# Runtime

Player actions, phase transitions, battle state, NPC behavior, multiplayer authority and persistence belong in this directory. Implementation has not started.

Keep authoritative state separate from presentation so the same result can be reproduced across clients. Define subsystem interfaces around Godot and the selected battle model before creating a class hierarchy.
