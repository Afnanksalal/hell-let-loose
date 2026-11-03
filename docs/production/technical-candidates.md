# Architecture evaluation

No engine or runtime stack has been selected. The decision depends on battle format, character animation, asset layering, networking and the available development capacity.

## Candidate stack

Godot with a 2D renderer and GDScript or C# is one option. ENet, versioned JSON or binary saves, authored event graphs and the engine's audio tools would support an initial evaluation. Other choices remain open until compared against a small working experiment.

## Shared state

An authoritative host is the current networking candidate. It would own inventory, NPC decisions, combat results, event selection and campaign changes. Clients present input, animation, sound and interface state. Movement prediction and interpolation depend on the movement model.

Synchronize important interactive objects before attempting a fully networked household physics simulation. Day and night should share entity and state definitions.

## Persistence and interruption

Campaign data includes chapter, completed missions, households, relationships, corruption and choices. Personal unlocks need separate ownership. Save versions require migration rules.

A disconnected character might temporarily sleep or enter a limited controlled state. Host loss could checkpoint progress and return to the lobby. Host migration needs a separate decision and implementation budget.

Matchmaking services, accounts, databases and dedicated servers should be added when a demonstrated requirement calls for them. Repository layout is described in [game](../../game/README.md).
