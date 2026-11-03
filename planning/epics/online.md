# Multiplayer authority and campaign saves

Keep actions and consequences consistent across clients and recover progress after interruption.

[Epic #17](https://github.com/Afnanksalal/hell-let-loose/issues/17) · [Design](../../docs/gameplay/multiplayer.md)

## Work items

### Define Godot shared-state architecture and two-client validation

[Issue #6](https://github.com/Afnanksalal/hell-let-loose/issues/6) · P0 · G1

- [ ] Use Godot; compare authority and transport choices within that engine.
- [ ] Define host ownership, replication and save boundaries.
- [ ] Document two-client validation and remaining bootstrap configuration.

### Implement host/join lobby and player readiness

[Issue #40](https://github.com/Afnanksalal/hell-let-loose/issues/40) · P1 · G1

- [ ] Host and join a local test session using the selected transport.
- [ ] Assign stable session player identifiers and an explicit authoritative host.
- [ ] Show ready/not-ready and rejection of invalid session transitions.
- [ ] Document local test setup without requiring a production account service.

Depends on: [#23](https://github.com/Afnanksalal/hell-let-loose/issues/23), [#6](https://github.com/Afnanksalal/hell-let-loose/issues/6).

### Synchronize interactions, phase state and battle requests

[Issue #41](https://github.com/Afnanksalal/hell-let-loose/issues/41) · P0 · G1

- [ ] Keep item ownership, household flags, phase transitions and encounter results consistent across two clients.
- [ ] Validate action requests at the host and reject duplicate or unauthorized changes.
- [ ] Separate state updates from client-only animation and UI.
- [ ] Record observed divergence and recovery behavior under delayed messages.

Depends on: [#40](https://github.com/Afnanksalal/hell-let-loose/issues/40), [#21](https://github.com/Afnanksalal/hell-let-loose/issues/21), [#20](https://github.com/Afnanksalal/hell-let-loose/issues/20), [#31](https://github.com/Afnanksalal/hell-let-loose/issues/31).

### Implement campaign/player save ownership and versioning

[Issue #43](https://github.com/Afnanksalal/hell-let-loose/issues/43) · P1 · G1

- [ ] Define ownership of campaign choices, personal customization and unlocks.
- [ ] Save and restore one full phase cycle without losing story or household state.
- [ ] Include a version marker and an explicit response to unsupported/corrupt data.
- [ ] Demonstrate a visitor keeping personal data separate from host campaign progress.

Depends on: [#6](https://github.com/Afnanksalal/hell-let-loose/issues/6), [#22](https://github.com/Afnanksalal/hell-let-loose/issues/22), [#21](https://github.com/Afnanksalal/hell-let-loose/issues/21).

### Handle player disconnects and host loss at checkpoints

[Issue #42](https://github.com/Afnanksalal/hell-let-loose/issues/42) · P1 · G2

- [ ] Define results for a disconnected participant in exploration and battle.
- [ ] Demonstrate reconnect/resume or a documented safe return path.
- [ ] Checkpoint and recover agreed progress after host loss.
- [ ] Verify item rewards and story outcomes are not duplicated on retry.

Depends on: [#41](https://github.com/Afnanksalal/hell-let-loose/issues/41), [#43](https://github.com/Afnanksalal/hell-let-loose/issues/43).
