# Progression, memory and generations

Define and implement progression toward adulthood without losing the meaning of character identity.

[Epic #18](https://github.com/Afnanksalal/hell-let-loose/issues/18) · [Design](../../docs/progression/aging-and-generations.md)

## Work items

### Define aging, memory loss and generation boundaries

[Issue #7](https://github.com/Afnanksalal/hell-let-loose/issues/7) · P2 · G2

- [ ] Describe aging triggers, mixed-age parties and the effects of forgetting.
- [ ] Separate narrative memory loss from player collection persistence.
- [ ] Decide which generational content belongs in the first game.

### Implement scoped rewards and equipment progression

[Issue #44](https://github.com/Afnanksalal/hell-let-loose/issues/44) · P2 · G2

- [ ] Choose a minimal reward model with an identified use for each resource.
- [ ] Implement an upgrade that adds a function rather than only damage.
- [ ] Persist unlocks under the agreed ownership rules.
- [ ] Test repeat rewards and failed missions for duplication or unwanted loss.

Depends on: [#22](https://github.com/Afnanksalal/hell-let-loose/issues/22), [#43](https://github.com/Afnanksalal/hell-let-loose/issues/43), [#29](https://github.com/Afnanksalal/hell-let-loose/issues/29).

### Specify and prototype age transitions and mixed-age parties

[Issue #45](https://github.com/Afnanksalal/hell-let-loose/issues/45) · P2 · G3

- [ ] Implement the agreed age trigger without coupling it to every short session.
- [ ] Show one transition preserving the intended character identity and data.
- [ ] Define a valid result for friends at different progression stages.
- [ ] Record content, customization and scene requirements for each committed stage.

Depends on: [#7](https://github.com/Afnanksalal/hell-let-loose/issues/7), [#43](https://github.com/Afnanksalal/hell-let-loose/issues/43).

### Prototype memories, fading identity and preserved player collections

[Issue #46](https://github.com/Afnanksalal/hell-let-loose/issues/46) · P2 · G3

- [ ] Capture a memory from a real event or relationship.
- [ ] Demonstrate its agreed fading/recovery behavior.
- [ ] Keep narrative forgetting distinct from unintended save or cosmetic deletion.
- [ ] Document what the finale can reliably refer back to.

Depends on: [#45](https://github.com/Afnanksalal/hell-let-loose/issues/45), [#38](https://github.com/Afnanksalal/hell-let-loose/issues/38).

### Define the finale and next-generation inheritance contract

[Issue #47](https://github.com/Afnanksalal/hell-let-loose/issues/47) · P2 · G3

- [ ] Select the first-game ending scope and where the next generation becomes playable.
- [ ] Define the world, character and account data that transfers or archives.
- [ ] List unresolved sequel ideas separately from the committed release scope.
- [ ] Provide a migration/recovery plan before implementing irreversible generation transitions.

Depends on: [#46](https://github.com/Afnanksalal/hell-let-loose/issues/46), [#7](https://github.com/Afnanksalal/hell-let-loose/issues/7).
