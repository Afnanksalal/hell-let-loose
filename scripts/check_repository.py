"""Dependency-free knowledge-base and release-evidence checks."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlparse

REQUIRED = ['README.md', 'AGENTS.md', 'CONTRIBUTING.md', 'CHANGELOG.md',
            'docs/vision.md', 'docs/continuity.md', 'decisions/register.md',
            'sources/README.md', 'docs/process/release-gates.md',
            'planning/backlog.json', 'releases/gates.json', 'releases/evidence.json']


def evidence_exists(root, value):
    if not isinstance(value, str) or not value.strip():
        return False
    if value.startswith('https://'):
        return bool(urlparse(value).hostname)
    path = (root / value.split('#')[0]).resolve()
    return path.is_relative_to(root.resolve()) and path.is_file()


def check(root, release=False):
    root = Path(root)
    errors = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f'Missing required file: {name}')
    version = (root / 'VERSION').read_text(encoding='utf-8').strip() if (root / 'VERSION').exists() else ''
    if not re.fullmatch(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)', version):
        errors.append('VERSION must contain a stable major.minor.patch value')

    for p in root.rglob('*'):
        if not p.is_file() or any(part in {'.git', '__pycache__', 'work'} for part in p.relative_to(root).parts):
            continue
        if p.suffix not in {'.md', '.json', '.yml', '.yaml', '.txt', '.py'}:
            continue
        text = p.read_text(encoding='utf-8')
        # Construct signatures rather than placing a matching credential in this checker.
        patterns = [r'gh[pousr]_' + r'[A-Za-z0-9]{30,}',
                    'github_' + r'pat_[A-Za-z0-9_]{30,}',
                    '-----BEGIN ' + r'(?:RSA |EC |OPENSSH )?PRIVATE KEY-----']
        if any(re.search(pattern, text) for pattern in patterns):
            errors.append(f'Potential credential/private key: {p.relative_to(root)}')
        if p.suffix != '.md':
            continue
        # This repository uses inline links; ignore fenced illustrative code.
        prose = re.sub(r'```.*?```', '', text, flags=re.S)
        for dest in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', prose):
            dest = dest.strip().strip('<>')
            if urlparse(dest).scheme or dest.startswith('#'):
                continue
            target = (p.parent / unquote(dest.split('#')[0])).resolve()
            if not target.is_relative_to(root.resolve()) or not target.exists():
                errors.append(f'Broken local link: {p.relative_to(root)} -> {dest}')

    try:
        gates = json.loads((root / 'releases/gates.json').read_text(encoding='utf-8'))
        data = json.loads((root / 'releases/evidence.json').read_text(encoding='utf-8'))
        if data['version'] != version:
            errors.append('Release evidence version differs from VERSION')
        if data['gate'] not in gates:
            errors.append('Unknown release gate')
        if data['kind'] not in {'knowledge-base', 'prototype', 'vertical-slice', 'alpha', 'beta', 'game'}:
            errors.append('Unknown release kind')
        gate_kind = {'G0':'knowledge-base','G1':'prototype','G2':'vertical-slice','G3':'alpha','G4':'beta','G5':'game'}
        if gate_kind.get(data['gate']) != data['kind']:
            errors.append('Release kind does not match gate')
        criteria = data['criteria']
        ids = [c['id'] for c in criteria]
        if len(ids) != len(set(ids)) or set(ids) != set(gates.get(data['gate'], [])):
            errors.append('Release criteria must exactly match the selected gate without duplicates')
        for c in criteria:
            if c['status'] not in {'pending', 'pass', 'fail'}:
                errors.append(f'Invalid criterion status: {c["id"]}')
            if not isinstance(c['evidence'], list):
                errors.append(f'Evidence must be a list: {c["id"]}')
                continue
            if c['status'] == 'pass' and (not c['evidence'] or not all(evidence_exists(root, v) for v in c['evidence'])):
                errors.append(f'Passing criterion lacks valid evidence: {c["id"]}')
            if release and c['status'] != 'pass':
                errors.append(f'Release blocked by {c["id"]}: {c["status"]}')
        if not (root / f'releases/{version}.md').is_file():
            errors.append('Versioned release notes missing')
        if release and version not in (root / 'CHANGELOG.md').read_text(encoding='utf-8'):
            errors.append('Release version missing from changelog')
        backlog = json.loads((root / 'planning/backlog.json').read_text(encoding='utf-8'))
        for task in backlog:
            if not task['title'] or not task['acceptance'] or task['gate'] not in gates:
                errors.append('Backlog task lacks title, acceptance criteria or valid gate')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f'Invalid planning/release manifest: {exc}')
    return errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--release', action='store_true', help='Require all selected release-gate criteria to pass')
    args = parser.parse_args()
    problems = check(args.root, args.release)
    for problem in problems:
        print(f'ERROR: {problem}')
    if problems:
        raise SystemExit(1)
    print('Repository checks passed' + ('; selected release gate passed' if args.release else ''))
