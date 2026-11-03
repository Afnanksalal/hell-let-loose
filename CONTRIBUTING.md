# Contributing

This is a source-available project with all rights reserved. Read [LICENSE](LICENSE) before reusing repository material. Feedback and bug reports are welcome; arrange permission with the maintainer before preparing code or asset contributions.

## Issues

Check existing issues first. For a defect, include the affected version, reproduction steps, expected behavior and actual result. For a design change, describe the problem, options and tradeoffs. Keep reference-game comparisons out of issue titles and public pitches; explain the desired behavior directly.

## Authorized development

1. Read the relevant design document and check whether the decision is settled.
2. Agree on a bounded issue with acceptance criteria and dependencies.
3. Branch from current main using `docs/123-topic`, `feat/123-topic`, `fix/123-topic` or `chore/123-topic`.
4. Keep commits focused. Update the affected documentation and decision record when behavior changes.
5. Open a pull request with its issue and validation evidence. Checks must pass and review conversations must be resolved before squash merge.

Commit subjects should state the change, for example `fix(save): preserve household state on reconnect`. Never commit credentials, imported assets without permission or generated engine caches.

## Validation

GitHub Actions checks Markdown style and local links. With Node.js available, the equivalent style check is `npx markdownlint-cli2@0.21.0 "**/*.md"`. Runtime build and test commands will be documented with Godot integration.

An issue is ready when its outcome, acceptance criteria and dependencies are clear. It is done when the work meets those criteria, its evidence is linked and the relevant PR or decision is accepted. Closing a design task does not establish that a game feature is implemented.

See [workflow](docs/process/project-board.md), [version control](docs/process/version-control.md) and [release gates](docs/process/release-gates.md).
