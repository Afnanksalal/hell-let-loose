# Release procedure

1. Open an issue describing release scope and gate. Do not call a design baseline a playable game.
2. In a topic branch, update VERSION, CHANGELOG.md, releases/evidence.json and the version's release notes.
3. Supply evidence for every criterion defined for the selected gate. Update the gate criteria through review if scope legitimately changes, never silently waive them.
4. Run repository checks, checker tests and `python scripts/check_repository.py --release`. For future playable releases, add actual build/playtest evidence before passing their gates.
5. Merge the release PR after required CI passes.
6. The owner manually runs **Release** on main. The workflow rechecks evidence and version, refuses an existing tag, tags that exact commit and publishes notes. It does not run on arbitrary tag pushes.
7. Verify the release page and evidence links. Update issues/Project status. If a release is wrong, publish a corrective patch; do not move a published tag.

The release workflow's write token exists only in its publish job. CI otherwise has read-only contents permissions. There are no account-level secrets in the repository. G0 needs repository evidence; higher gates need real implementation evidence, not just a populated form.
