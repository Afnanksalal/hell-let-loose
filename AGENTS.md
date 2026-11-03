# Repository instructions

## Project context

This repository is the home of the full game: runtime code, original assets, tests and documentation. It is currently in pre-production. Read README.md, docs/vision.md, docs/continuity.md and decisions/register.md before changing the design. Read the relevant subsystem document before implementing it.

## Design and writing

- Describe the game's own behavior. Keep reference titles and comparison-based pitches out of public descriptions, topics, issues and design documents.
- Write plain technical and design prose. Avoid promotional claims, chat transcripts and repeated commentary about how a document was produced.
- Preserve agreed direction, but keep unresolved choices in the decision register. Draft lore and example moves do not become requirements by being documented.
- Preserve the daytime/nighttime consequence loop, broad customization, tactical battles, comic narration and the adulthood/memory/generation arc.
- Treat specific joke attacks, cooldowns, age bands and example episodes as drafts until accepted.

## Development

Read CONTRIBUTING.md and docs/process/version-control.md. Use issue-linked branches and pull requests. Main requires passing Repository checks and resolved review conversations. Do not add a build badge or claim a playable feature before an actual build exists.

Keep runtime implementation under game/, original assets under assets/ and game tests under tests/. Select the engine through a recorded decision before adding its project files. Add tools only when development requires them; do not generate a scripts directory or placeholder checker suite.

Update relevant documentation and the decision register when a choice changes. Keep release evidence current. Do not publish a release without its applicable gate. Respect LICENSE; this is source-available with all rights reserved, not FOSS. Do not import code or assets without compatible permission and provenance.

Maintain workflow dependencies manually. Do not add Dependabot configuration or enable its automation.
