# Contributing

Read [AGENTS.md](AGENTS.md), the [vision](docs/vision.md) and [decision register](decisions/register.md) before proposing changes. This is currently a design repository, not a playable game.

## Working process

1. Open an issue with the problem, scope and acceptance criteria. Use a design decision issue for unsettled mechanics.
2. Move it through the [project workflow](docs/process/project-board.md). Implementation starts only when its scope is agreed.
3. Branch from current main: `docs/123-topic`, `feat/123-topic`, `fix/123-topic` or `chore/123-topic`.
4. Make focused commits such as `docs(story): clarify generational ending`. Never commit credentials, personal exports or unlicensed reference assets.
5. Update the primary topic, decision register and changelog where direction changes. Distinguish user direction from proposals.
6. Run `python scripts/check_repository.py` and `python -m unittest discover -s tests -v`.
7. Open a PR using the template, link its issue and include validation evidence. Required checks must pass; resolve conversations before squash merge.
8. Close the linked issue, mark it Done and delete the merged topic branch.

Use PRs even as a solo maintainer: self-review is allowed; a second-person approval is not required because that would lock a solo repository. Future collaborators can add review requirements deliberately.

## Definition of ready

An issue has a bounded outcome, acceptance criteria, area, priority, milestone and dependencies. Unknown design choices are explicitly listed. Ready for implementation does not mean every brainstorm is approved.

## Definition of done

Acceptance criteria met; appropriate checks/evidence linked; docs and decisions current; no unresolved blocking comments. A closed planning issue does not prove a game feature exists.

See [version control](docs/process/version-control.md), [release gates](docs/process/release-gates.md) and [release procedure](docs/process/releasing.md).
