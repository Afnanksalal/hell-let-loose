# Neighborhood story and narration

Deliver one authored incident across day, night and the next morning, with meaningful branches and narration.

[Epic #16](https://github.com/Afnanksalal/hell-let-loose/issues/16) · [Design](../../docs/narrative/story-director.md)

## Work items

### Outline the first connected story episode

[Issue #5](https://github.com/Afnanksalal/hell-let-loose/issues/5) · P1 · G1

- [ ] Connect a daytime choice, sunset complication, battle and next-day consequence.
- [ ] Place narration and alternate outcomes around player choices.
- [ ] Settle the episode scope and identify any unresolved setting details.

### Implement authored event prerequisites and persistent outcomes

[Issue #37](https://github.com/Afnanksalal/hell-let-loose/issues/37) · P1 · G1

- [ ] Load an authored event with participants, prerequisites and outcome effects.
- [ ] Prevent incompatible event branches from creating contradictory state.
- [ ] Handle an unavailable participant or interrupted objective explicitly.
- [ ] Show a story flag affecting later phase eligibility.

Depends on: [#22](https://github.com/Afnanksalal/hell-let-loose/issues/22), [#21](https://github.com/Afnanksalal/hell-let-loose/issues/21).

### Build the first branching day-to-night episode

[Issue #36](https://github.com/Afnanksalal/hell-let-loose/issues/36) · P1 · G2

- [ ] Select and implement one episode rather than treating all story studies as committed content.
- [ ] Support a meaningful daytime branch, nighttime resolution and next-day consequence.
- [ ] Document party-choice handling and a failure path.
- [ ] Run a complete session and attach the observed narrative and pacing problems.

Depends on: [#5](https://github.com/Afnanksalal/hell-let-loose/issues/5), [#37](https://github.com/Afnanksalal/hell-let-loose/issues/37), [#29](https://github.com/Afnanksalal/hell-let-loose/issues/29), [#26](https://github.com/Afnanksalal/hell-let-loose/issues/26).

### Integrate narration, subtitles and story callbacks

[Issue #39](https://github.com/Afnanksalal/hell-let-loose/issues/39) · P1 · G2

- [ ] Place narration at selected discoveries and consequences rather than every action.
- [ ] Provide readable subtitles and volume/mute controls.
- [ ] Demonstrate a callback that uses a real prior session choice.
- [ ] Record voice, text and audio rights; identify localization requirements.

Depends on: [#36](https://github.com/Afnanksalal/hell-let-loose/issues/36).

### Add the story journal and clue persistence

[Issue #38](https://github.com/Afnanksalal/hell-let-loose/issues/38) · P2 · G2

- [ ] Show current objectives and discovered clues without exposing undiscovered branches.
- [ ] Restore journal state after save/load and reconnect.
- [ ] Define what is shared with the party and what is character-specific.
- [ ] Test an episode with a player who missed its initial clue.

Depends on: [#37](https://github.com/Afnanksalal/hell-let-loose/issues/37), [#43](https://github.com/Afnanksalal/hell-let-loose/issues/43).
