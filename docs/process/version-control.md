# Version control policy

## Branches and merges

`main` holds reviewed work. Use short-lived issue-linked branches; avoid a permanent develop branch. Squash merge PRs, delete merged branches and do not force-push or delete main. Revert through a new PR rather than rewriting published history.

Main requires a pull request, current passing `Repository checks`, resolved review conversations and linear history. No bypass actors are configured. Zero required external approvals supports a solo maintainer while retaining an auditable PR and CI gate.

Suggested commits: `docs(area): change`, `feat(area): change`, `fix(area): change`, `chore(area): change`, `test(area): change`. CI does not rewrite or enforce historical commit messages.

## Versions

VERSION is the source of truth. Use SemVer-shaped versions: major for incompatible supported game/save contracts after 1.0, minor for meaningful pre-1.0 milestones, patch for corrections to the current baseline. Pre-1.0 compatibility is described explicitly in release notes.

0.1.0 is reserved for the knowledge-base foundation, not a playable build. Later prototype and slice versions require their own gates. A version file alone is not a published release. Release tags are `v` followed by VERSION and must identify a commit on main. Do not move published tags; issue a new patch release.

## Ownership and public contents

Public visibility is not an open-source license grant. No license was chosen by the owner. Reference games guide qualities; their assets are not included. Track future asset provenance before a playable release. No credentials or shared-chat account sessions belong here.

The initial public push bootstraps the repository. After protection is enabled, all changes follow PRs. See [release process](releasing.md).
