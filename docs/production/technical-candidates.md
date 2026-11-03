# Godot architecture evaluation

Godot is the selected engine. [Project architecture](../architecture/godot.md) defines the repository boundary and the configuration choices needed at bootstrap. The exact version, renderer, language and test runner remain open.

## Shared state

An authoritative host is the networking candidate. It owns inventory changes, NPC decisions, combat results, event selection and campaign changes. Clients send actions and present the resulting state. Movement prediction depends on the movement model; battles need explicit ordering and validation rules.

Synchronize important interactive objects before attempting a fully networked household physics simulation. Day and night read the same campaign state.

## Content and persistence

Evaluate Godot Resources for moves, items, character parts and event definitions. Definitions need stable identifiers and validation. Keep save data separate from scene instances so content and save formats can evolve independently.

Campaign data includes chapters, missions, households, relationships, corruption and choices. Personal collections have separate ownership. Define interruption checkpoints and version migration before relying on persistence.

## Dependencies

Choose networking transport, test runner and any editor extensions through their issues. A disconnected player or lost host must have a documented result. Dedicated services and host migration need demonstrated requirements before implementation.
