# Game source

The game runtime belongs here. Engine integration has not started; no build command is available yet.

| Directory | Responsibility |
| --- | --- |
| [runtime](runtime/README.md) | Player actions, phase state, battles, NPC behavior, networking and persistence |
| [scenes](scenes/README.md) | World locations, encounters and reusable scene composition |
| [data](data/README.md) | Authored moves, items, customization definitions and story events |
| [ui](ui/README.md) | Menus, character creation, HUD, journal and interaction presentation |

Keep source assets in [assets](../assets/README.md) and runtime tests in [tests](../tests/README.md). The engine decision may adjust these boundaries where its resource model requires it. Record that decision before adding project files.
