# Technical candidates

**All technical choices are proposals. No engine is selected.** [Earlier source](../../sources/chat-01.md).

Earlier candidates: Godot 4, GDScript/C#, 2D rendering, ENet, versioned JSON/binary saves, data-driven event graphs, Aseprite/LibreSprite and built-in audio or FMOD. Pixel-art tooling advice predates FNF and requires reconsideration.

An authoritative listen-server could own world state, NPC behavior, inventory, combat outcomes, missions and event selection. Clients handle input, UI, animation/audio and appropriate movement prediction/interpolation. Synchronize important objects rather than every household physics object. Battle authority must follow the chosen battle rules.

NPC routines could use behavior trees or hierarchical state machines. Day and night share entities, inventory, statuses and persistent state.

Save chapter, missions, locations, households, relationships, corruption and choices separately from personal unlocks. Version saves for migration. Disconnect proposal: temporarily sleeping/limited AI player; checkpoint/return to lobby after host loss. Host migration is not promised.

Matchmaking/accounts, PostgreSQL, Docker and later dedicated servers are historical options, not infrastructure to provision now. Decide camera, battles, art pipeline and playable scope before treating the old stack as a commitment.
