# Playtesting and release readiness

Progress from a complete vertical slice to a supported build through inspectable test and distribution evidence.

[Epic #19](https://github.com/Afnanksalal/hell-let-loose/issues/19) · [Design](../../docs/process/release-gates.md)

## Work items

### Set vertical-slice scope and playtest evidence targets

[Issue #8](https://github.com/Afnanksalal/hell-let-loose/issues/8) · P2 · G2

- [ ] Scope a complete session after the battle, art and architecture decisions.
- [ ] Define external playtest acceptance targets.
- [ ] Specify build, save/load and reconnect evidence needed for G2.

### Run an external vertical-slice playtest and record findings

[Issue #48](https://github.com/Afnanksalal/hell-let-loose/issues/48) · P1 · G2

- [ ] Test a complete target-length session with participants who did not build it.
- [ ] Record onboarding, waiting time, daytime enjoyment and story comprehension.
- [ ] Attach build/commit identifiers and actionable observations.
- [ ] File follow-up defects and state whether the slice acceptance targets were met.

Depends on: [#8](https://github.com/Afnanksalal/hell-let-loose/issues/8), [#36](https://github.com/Afnanksalal/hell-let-loose/issues/36), [#32](https://github.com/Afnanksalal/hell-let-loose/issues/32), [#42](https://github.com/Afnanksalal/hell-let-loose/issues/42), [#39](https://github.com/Afnanksalal/hell-let-loose/issues/39).

### Review input, subtitles, readability and non-voice coordination

[Issue #49](https://github.com/Afnanksalal/hell-let-loose/issues/49) · P1 · G4

- [ ] Review keyboard/controller navigation, focus, text sizing and contrast in actual screens.
- [ ] Test subtitle readability and sound/narration controls.
- [ ] Verify essential coordination works without a microphone.
- [ ] Document findings, fixes and remaining limitations against the chosen targets.

Depends on: [#32](https://github.com/Afnanksalal/hell-let-loose/issues/32), [#39](https://github.com/Afnanksalal/hell-let-loose/issues/39), [#40](https://github.com/Afnanksalal/hell-let-loose/issues/40).

### Measure frame time, network load and target-party stability

[Issue #50](https://github.com/Afnanksalal/hell-let-loose/issues/50) · P1 · G4

- [ ] Define performance targets and name representative hardware and network conditions.
- [ ] Profile actual scenes and encounters with the target party size.
- [ ] Record frame-time, memory and network observations with build identifiers.
- [ ] Fix release-blocking regressions and retain reproducible measurement steps.

Depends on: [#30](https://github.com/Afnanksalal/hell-let-loose/issues/30), [#42](https://github.com/Afnanksalal/hell-let-loose/issues/42), [#34](https://github.com/Afnanksalal/hell-let-loose/issues/34).

### Prepare supported builds, notices and release recovery

[Issue #51](https://github.com/Afnanksalal/hell-let-loose/issues/51) · P1 · G5

- [ ] Choose supported platforms and produce reproducible exports with hashes.
- [ ] Verify final naming, original asset provenance and third-party notices.
- [ ] Document known issues, save backup/recovery and support scope.
- [ ] Obtain the owner go/no-go and attach all G5 evidence before publishing.

Depends on: [#48](https://github.com/Afnanksalal/hell-let-loose/issues/48), [#49](https://github.com/Afnanksalal/hell-let-loose/issues/49), [#50](https://github.com/Afnanksalal/hell-let-loose/issues/50), [#47](https://github.com/Afnanksalal/hell-let-loose/issues/47).
