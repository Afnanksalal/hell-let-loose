# Publishing a release

1. Open an issue for the release scope and gate.
2. In a topic branch, update VERSION, CHANGELOG.md, the versioned release notes and releases/evidence.json.
3. Supply evidence for every criterion in the selected gate. Higher milestones need actual build and playtest records.
4. Open a release PR. Check version consistency and evidence during review; required repository checks must pass.
5. Merge the PR, then request the Release workflow on main from the owner account.
6. Verify the release page, tag and evidence links. Update the issue and project status.

The workflow validates the manifest and refuses a pending criterion or an existing tag. A failed publication can leave a tag without release notes; recover by inspecting that tag and publishing notes for its verified commit, never by moving it. Corrections to a published release use a new patch version.

CI has read-only repository permissions. Only the release publish job receives contents-write permission. The repository currently has no playable release or game-build workflow.
