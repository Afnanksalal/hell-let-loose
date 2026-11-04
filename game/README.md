# Game source

The first room is a runnable input preview. See the [root README](../README.md) for editor, run and export commands.

| Directory | Responsibility |
| --- | --- |
| [runtime](runtime/README.md) | Player actions, phase state, battles, NPC behavior, networking and persistence |
| [scenes](scenes/README.md) | World locations, encounters and reusable scene composition |
| [data](data/README.md) | Authored moves, items, customization definitions and story events |
| [ui](ui/README.md) | Menus, character creation, HUD, journal and interaction presentation |

Keep source assets in [assets](../assets/README.md) and runtime tests in [tests](../tests/README.md). The repository root is the Godot project root, making game/ and assets/ available under res://. See [Godot architecture](../docs/architecture/godot.md) for version selection and resource rules.
