# Godot project foundation

Establish a reproducible Godot project and the shared runtime boundaries needed by the prototype.

[Epic #12](https://github.com/Afnanksalal/hell-let-loose/issues/12) · [Design](../../docs/architecture/godot.md)

## Work items

### Bootstrap the Godot project and pin its configuration

[Issue #23](https://github.com/Afnanksalal/hell-let-loose/issues/23) · P0 · G1

- [ ] Record the exact supported Godot release, renderer and language with reasons for the selection.
- [ ] Add project.godot at the repository root, a working entry scene and input actions.
- [ ] Document editor/run commands and show a clean checkout importing and starting without missing resources.
- [ ] Keep generated caches and credentials out of Git; add a real headless import check once runnable.

### Define shared session state and phase transitions

[Issue #21](https://github.com/Afnanksalal/hell-let-loose/issues/21) · P0 · G1

- [ ] Define day, sunset, night, dawn and result states with explicit transition conditions.
- [ ] Separate authoritative state from UI and scene presentation.
- [ ] Demonstrate that carried items and one household flag survive a complete cycle.
- [ ] Cover duplicate transition requests and interruption at a phase boundary.

Depends on: [#23](https://github.com/Afnanksalal/hell-let-loose/issues/23).

### Implement movement and contextual object interaction

[Issue #20](https://github.com/Afnanksalal/hell-let-loose/issues/20) · P1 · G1

- [ ] Choose and document camera/input behavior; implement movement in a small test room.
- [ ] Support inspect, pick up, use and put down for a limited object set with clear feedback.
- [ ] Prevent competing interaction requests from duplicating or losing an object.
- [ ] Record controller and keyboard interaction requirements before expanding content.

Depends on: [#23](https://github.com/Afnanksalal/hell-let-loose/issues/23).

### Define Godot resources for authored gameplay data

[Issue #22](https://github.com/Afnanksalal/hell-let-loose/issues/22) · P1 · G1

- [ ] Choose the representation for items, moves, character parts and story definitions.
- [ ] Use stable identifiers and validate missing or duplicate references.
- [ ] Load one usable example of each required definition without file-order dependencies.
- [ ] Document how localization keys and save compatibility refer to the definitions.

Depends on: [#23](https://github.com/Afnanksalal/hell-let-loose/issues/23).
