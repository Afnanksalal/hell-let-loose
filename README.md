# Hell Let Loose

A cooperative supernatural comedy game about babies with a secret life after bedtime.

During the day, take care of yourself, make friends, sneak around the house and get into trouble. At night, escape your crib and meet the others to deal with whatever has crawled into the neighborhood. The things you ate, stole or broke earlier can change your abilities and the trouble waiting outside. Get home before your parents wake up.

## Development status

The game is in pre-production. This repository will contain the complete game source, original assets and development tools. The design documents and repository workflow are in place; a playable build and engine integration have not been added yet.

The current target is cooperative play for 2 to 8 players, with sessions of roughly 20 to 30 minutes. Battle pacing, networking and customization scope are the next design decisions.

## The game

- Daytime care, exploration and small household heists affect the night's adventure.
- Battles use distinct moves, status effects and cooperative tactics. The turn format is still being evaluated.
- Character customization covers appearance and personality, with equipment and behavior affecting play.
- An authored mystery runs through the neighborhood's changing households and supernatural incidents.
- Over the campaign, the children grow up and begin forgetting who they were. Their story ends as a new generation appears.

The visual direction uses bold outlines, expressive faces, exaggerated poses and strong color. Comedy comes from the characters and their decisions; the mystery gives those decisions consequences.

## Repository layout

| Directory | Contents |
| --- | --- |
| [game](game/README.md) | Runtime code, scenes, game data and interface implementation |
| [assets](assets/README.md) | Original character, environment, interface and audio assets |
| [tests](tests/README.md) | Future runtime, integration and gameplay tests |
| [docs](docs/README.md) | Game design, architecture decisions and development process |
| [planning](planning/README.md) | Initial backlog and GitHub tracking references |
| [releases](releases/README.md) | Release criteria, evidence and notes |
| [.github](.github/README.md) | Checks, issue templates and repository rules |

## Development

Start with the [game overview](docs/vision.md), [session sequence](docs/continuity.md) and [decision register](decisions/register.md). The [roadmap](docs/production/roadmap.md) describes what needs to be proven before a playable release. Engine-specific build instructions will accompany the first runtime implementation.

[Project board](https://github.com/users/Afnanksalal/projects/3) · [Issues](https://github.com/Afnanksalal/hell-let-loose/issues) · [Checks](https://github.com/Afnanksalal/hell-let-loose/actions/workflows/checks.yml)

## Feedback and rights

Bug reports and design feedback are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting work. This is a public, source-available project with all rights reserved. You may study it and draw inspiration for independently created work; reuse, redistribution and sale of repository material require permission. See [LICENSE](LICENSE) for the terms and the GitHub platform exception.
