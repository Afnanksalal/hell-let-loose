import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('checker', ROOT / 'scripts/check_repository.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class RepositoryChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / 'repo'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__', 'work'))

    def tearDown(self):
        self.tmp.cleanup()

    def manifest(self, mutate):
        p = self.root / 'releases/evidence.json'
        data = json.loads(p.read_text(encoding='utf-8'))
        mutate(data)
        p.write_text(json.dumps(data), encoding='utf-8')

    def test_repository_valid(self):
        self.assertEqual(checker.check(self.root), [])

    def test_broken_link_fails(self):
        with (self.root / 'README.md').open('a', encoding='utf-8') as f:
            f.write('\n[missing](does-not-exist.md)\n')
        self.assertTrue(any('Broken local link' in x for x in checker.check(self.root)))

    def test_link_cannot_escape_repository(self):
        with (self.root / 'README.md').open('a', encoding='utf-8') as f:
            f.write('\n[escape](../outside.md)\n')
        self.assertTrue(any('Broken local link' in x for x in checker.check(self.root)))

    def test_pending_gate_blocks_release(self):
        self.manifest(lambda d: d['criteria'][0].update(status='pending'))
        self.assertTrue(any('Release blocked' in x for x in checker.check(self.root, True)))

    def test_pass_needs_evidence(self):
        self.manifest(lambda d: d['criteria'][0].update(status='pass', evidence=[]))
        self.assertTrue(any('lacks valid evidence' in x for x in checker.check(self.root)))

    def test_missing_criterion_fails(self):
        self.manifest(lambda d: d['criteria'].pop())
        self.assertTrue(any('exactly match' in x for x in checker.check(self.root)))

    def test_version_mismatch_fails(self):
        self.manifest(lambda d: d.update(version='9.9.9'))
        self.assertTrue(any('differs from VERSION' in x for x in checker.check(self.root)))

    def test_credential_pattern_fails(self):
        (self.root / 'leak.txt').write_text('ghp' + '_' + 'A' * 36, encoding='utf-8')
        self.assertTrue(any('Potential credential' in x for x in checker.check(self.root)))

    def test_duplicate_criterion_fails(self):
        self.manifest(lambda d: d['criteria'].append(d['criteria'][0]))
        self.assertTrue(any('exactly match' in x for x in checker.check(self.root)))

    def test_kind_gate_mismatch_fails(self):
        self.manifest(lambda d: d.update(kind='game'))
        self.assertTrue(any('kind does not match' in x for x in checker.check(self.root)))


if __name__ == '__main__':
    unittest.main()
