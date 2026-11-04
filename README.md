# Hell Let Loose

The adults think everyone is asleep. The babies are climbing out of their cribs to find out what has been haunting the neighborhood.

Hell Let Loose is a cooperative supernatural comedy about growing up with a secret. During the day, you explore your home, make friends, and try to get away with small acts of mischief. After bedtime, you meet up with the other babies, investigate hauntings, and fight whatever turns up. Then you have to get home before your parents wake up.

**Current build:** a runnable Godot room preview. The campaign and cooperative play are planned. [Run the preview](#run-the-preview)

## How a session plays

1. **Day.** Eat, rest, explore, and prepare for the night. A stolen flashlight might reveal an enemy later. A broken vase might leave a parent watching the hallway when you need to sneak out. What you do during the day can also change which powers you have at night.
2. **Bedtime.** Slip out of the house and help any friends who are still stuck inside.
3. **Night.** Follow a clue or deal with a supernatural incident. Battles are built around distinct moves, status effects, and ways to help your friends. The exact turn format is still open.
4. **Morning.** Get back to bed and deal with the evidence. The night's outcome can change household routines and what happens the next day.

The target is **2 to 8 players** and **20 to 30 minutes per session**. Character customization includes appearance, clothing, expressions, movement, and habits. Equipment and behavior can affect play, so there is room to build a character who looks and acts like yours.

## What happens as you grow up

The neighborhood mystery runs across sessions. Friendships change, new places open up, and the narrator can call back to earlier trouble. Characters grow from childhood through adolescence toward adulthood, gradually forgetting who they were. Eventually their story ends, and a new generation of babies inherits the neighborhood they left behind.

The visual direction is hand-drawn cartoon art with strong outlines, bright colors, and exaggerated expressions. The narration follows the kids as they take their very small lives and very large responsibilities seriously.

[Game design](docs/vision.md) · [Session and campaign sequence](docs/continuity.md) · [Visual direction](docs/art/direction.md)

## Run the preview

Install the standard **Godot 4.7.2** editor. Clone the repository, open [project.godot](project.godot) in Godot, and press **F5**. To launch from a terminal with Godot on PATH:

```powershell
git clone https://github.com/Afnanksalal/hell-let-loose.git
cd hell-let-loose
godot --path .
```

| Key | Action |
| --- | --- |
| **WASD** | Move the marker |
| **E** | Switch the room light |

To open the editor, run `godot --editor --path .`. [Godot downloads](https://godotengine.org/download/archive/4.7.2-stable/)

## Technology and tools

| Area | Choice |
| --- | --- |
| Engine | Godot 4.7.2 with the Compatibility renderer |
| Game code | Typed GDScript |
| Scenes and input | Godot 2D scenes and the Godot Input Map |
| Builds | Windows x64 export preset |
| Art and audio | Krita for drawn art, Inkscape for vector assets, Audacity for recording and editing |
| CI | GitHub Actions runs Markdown lint, local link checks, and a headless Godot import and startup check |

A host that owns the shared game state is the current networking candidate. The transport, battle timing, and gameplay test runner are open decisions. [Architecture](docs/architecture/godot.md) · [Technical evaluation](docs/production/technical-candidates.md) · [Decision register](decisions/register.md)

### Check or export a build

Run the same import and startup commands used in CI:

```powershell
godot --headless --path . --editor --import
godot --headless --path . --quit-after 120 -- --smoke-test
```

For a local Windows build, install the matching **4.7.2 Windows x64 release template**, then run:

```powershell
New-Item -ItemType Directory -Force build | Out-Null
godot --headless --path . --export-release Windows build/hell-let-loose.exe
```

Keep the generated executable and its `.pck` file together.

## Development plan

| Milestone | What we want to demonstrate |
| --- | --- |
| Godot bootstrap (complete) | A clean checkout imports and runs the input preview and produces a Windows build. |
| Prototype | Two local clients share a household session. One daytime choice affects an escape or battle, and the outcome changes the next morning. Try a customization combination and a power gained through behavior. |
| Vertical slice | Play one complete authored episode with representative art, narration, save/load, and reconnect behavior. Test it with players outside the development team. |
| Later production | Expand the neighborhood and campaign, test the target party size, and develop aging, memory loss, and the handoff to the next generation. |

[Project board](https://github.com/users/Afnanksalal/projects/3) · [Implementation plan](planning/implementation-plan.md) · [Release gates](docs/process/release-gates.md)

## Repository layout

| Path | Contents |
| --- | --- |
| [game/](game/README.md) | Runtime code, scenes, game data, and interface files |
| [assets/](assets/README.md) | Character, environment, interface, and audio assets |
| [tests/](tests/README.md) | Game test organization and future coverage |
| [docs/](docs/README.md) | Design, architecture, and development process |
| [planning/](planning/README.md) | Epics, dependencies, and issue references |
| [releases/](releases/README.md) | Release criteria, evidence, and notes |
| [.github/](.github/WORKFLOWS.md) | Workflows, templates, and repository rules |

## Feedback and rights

Bug reports and design feedback are welcome through [GitHub Issues](https://github.com/Afnanksalal/hell-let-loose/issues). Contact the maintainer before preparing code or asset contributions. [Contribution guide](CONTRIBUTING.md) · [Security reporting](SECURITY.md)

The repository is **source-available, all rights reserved**. You may study the material and draw inspiration for independently created work. Reuse, redistribution, and sale require permission under the terms of the [rights notice](LICENSE), which also describes the GitHub platform exception. [Third-party notices](THIRD_PARTY.md)
