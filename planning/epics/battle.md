# Cooperative battle system

Choose and demonstrate a tactical battle format that keeps small and large parties involved.

[Epic #14](https://github.com/Afnanksalal/hell-let-loose/issues/14) · [Design](../../docs/gameplay/battles.md)

## Work items

### Decide cooperative battle format

[Issue #2](https://github.com/Afnanksalal/hell-let-loose/issues/2) · P0 · G1

- [ ] Compare sequential turns and simultaneous planning for small and large parties.
- [ ] Describe idle handling, coordination and transitions between exploration and encounters.
- [ ] Record the selected format and its consequences in the design documents.

### Implement deterministic action validation and battle resolution

[Issue #31](https://github.com/Afnanksalal/hell-let-loose/issues/31) · P0 · G1

- [ ] Represent battle participants, legal actions and action order independently of animation.
- [ ] Reject illegal, duplicate and late action requests.
- [ ] Resolve a small move set reproducibly from the same initial state and actions.
- [ ] Demonstrate victory, defeat and return to exploration with recorded state outcomes.

Depends on: [#2](https://github.com/Afnanksalal/hell-let-loose/issues/2), [#22](https://github.com/Afnanksalal/hell-let-loose/issues/22), [#21](https://github.com/Afnanksalal/hell-let-loose/issues/21).

### Add status effects, team interactions and recovery

[Issue #28](https://github.com/Afnanksalal/hell-let-loose/issues/28) · P1 · G1

- [ ] Define status timing, duration, stacking and removal rules for the prototype move set.
- [ ] Demonstrate one cooperative combination with clear cause and effect.
- [ ] Choose and implement the downed/recovery behavior for the selected battle format.
- [ ] Verify total defeat creates the intended session outcome without corrupting state.

Depends on: [#31](https://github.com/Afnanksalal/hell-let-loose/issues/31).

### Build one enemy encounter with a cooperative objective

[Issue #29](https://github.com/Afnanksalal/hell-let-loose/issues/29) · P1 · G1

- [ ] Create an enemy with readable intent and behavior beyond a health increase.
- [ ] Require a team action, environmental step or objective in addition to attacking.
- [ ] Provide understandable move, target and outcome feedback.
- [ ] Record small-party results and the changes needed before larger-party testing.

Depends on: [#31](https://github.com/Afnanksalal/hell-let-loose/issues/31), [#28](https://github.com/Afnanksalal/hell-let-loose/issues/28).

### Evaluate battle pacing and readability at target party sizes

[Issue #30](https://github.com/Afnanksalal/hell-let-loose/issues/30) · P1 · G2

- [ ] Measure planning/waiting time and action readability with small and target-sized parties.
- [ ] Test idle-player handling and simultaneous/conflicting requests.
- [ ] Set a documented encounter pacing target based on observations.
- [ ] List and prioritize format changes before expanding enemy content.

Depends on: [#29](https://github.com/Afnanksalal/hell-let-loose/issues/29), [#41](https://github.com/Afnanksalal/hell-let-loose/issues/41).
