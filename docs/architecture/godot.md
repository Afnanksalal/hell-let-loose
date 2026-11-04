# Godot project architecture

The project uses Godot 4.7.2 with typed GDScript. GDScript supports direct iteration in the editor and uses the standard Godot distribution. The Compatibility renderer is the starting point for the 2D prototype and supports OpenGL hardware.

## Project boundary

The root project.godot makes res://game/ and res://assets/ available to runtime scenes. Keep production code in game/runtime/, scene composition in game/scenes/, authored definitions in game/data/ and interface code in game/ui/.

Documentation and planning directories contain .gdignore markers so the editor does not import them. Keep the tests directory visible until the Godot test runner's discovery rules are chosen.

## Resources and source control

Use snake_case resource paths and PascalCase node names. Prefer text scenes and resources where they make reviews useful. Commit source and required import/UID metadata; do not ignore .uid files. Exclude the .godot cache, generated translations, export output and credentials.

Keep asset authorship and permissions in [provenance](../../assets/provenance.md). Editable art can sit beside its export until import exclusions and large-file handling are chosen for the production pipeline. Third-party plugins need identified terms and versions before entering addons/.

## Runtime responsibilities

| Area | Boundary to establish |
| --- | --- |
| Session | Phase clock, transitions, party readiness and authoritative phase state |
| Characters | Input, movement, interaction, needs and appearance composition |
| Battles | Move definitions, action validation, resolution order, status effects and outcomes |
| Households | Parent routines, suspicion, interactables, escape and return conditions |
| Story | Authored events, prerequisites, branch results and persistent flags |
| Networking | Authority, action requests, snapshots, client presentation and interruption |
| Saves | Campaign/player ownership, versioning, migration and checkpoint recovery |
| Interface | Views and input focus driven by runtime state |

These are responsibilities, not a mandated singleton or class hierarchy. Begin with the smallest coherent scenes and data interfaces needed for the prototype.

## First runnable project

The first room checks input wiring and scene loading. The Windows preset exports an x64 build. CI imports the project and runs the entry scene headlessly. See the [root README](../../README.md) for commands.

## References

Godot's [project organization guide](https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html) covers resource paths and import boundaries. Its [version-control guide](https://docs.godotengine.org/en/stable/tutorials/best_practices/version_control_systems.html) lists generated files to exclude. Engine upgrades require a reviewed change with import, save and representative-scene checks.
