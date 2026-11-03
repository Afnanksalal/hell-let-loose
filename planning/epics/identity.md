# Character identity and art pipeline

Support expressive original characters and compatible customization before expanding the wardrobe.

[Epic #15](https://github.com/Afnanksalal/hell-let-loose/issues/15) · [Design](../../docs/gameplay/customization.md)

## Work items

### Define customization scope and art pipeline

[Issue #3](https://github.com/Afnanksalal/hell-let-loose/issues/3) · P1 · G1

- [ ] Define initial customization dimensions and compatible outfit/body combinations.
- [ ] Specify original character shapes, expressions, animation and readability targets.
- [ ] Evaluate camera and animation production methods before asset production.

### Produce an original character and environment visual specification

[Issue #33](https://github.com/Afnanksalal/hell-let-loose/issues/33) · P1 · G1

- [ ] Define line, color, silhouette and expression rules with original studies.
- [ ] Show the same character and location during day and night.
- [ ] Identify camera and asset-resolution requirements for runtime import.
- [ ] Record authorship and usage permissions for every included production asset.

Depends on: [#3](https://github.com/Afnanksalal/hell-let-loose/issues/3).

### Prototype character part composition in Godot

[Issue #35](https://github.com/Afnanksalal/hell-let-loose/issues/35) · P1 · G1

- [ ] Implement a limited set of compatible body, clothing and accessory combinations.
- [ ] Specify layer order, attachment points and incompatible combinations.
- [ ] Check representative movement and battle poses for clipping and readability.
- [ ] Save and restore a character through stable part identifiers.

Depends on: [#33](https://github.com/Afnanksalal/hell-let-loose/issues/33), [#22](https://github.com/Afnanksalal/hell-let-loose/issues/22).

### Build character preview and customization selection

[Issue #32](https://github.com/Afnanksalal/hell-let-loose/issues/32) · P1 · G2

- [ ] Provide a preview with selectable parts and understandable feedback for unavailable combinations.
- [ ] Support keyboard/controller focus requirements chosen for the slice.
- [ ] Persist and restore the selected character; handle missing content gracefully.
- [ ] Verify one player can identify teammates through appearance in a group encounter.

Depends on: [#35](https://github.com/Afnanksalal/hell-let-loose/issues/35).

### Establish animation and asset import conventions

[Issue #34](https://github.com/Afnanksalal/hell-let-loose/issues/34) · P1 · G2

- [ ] Choose frame-by-frame or rigged production with a representative test.
- [ ] Document editable sources, exports, import settings and file naming.
- [ ] Demonstrate idle, movement, interaction and one attack across supported parts.
- [ ] Decide when Git LFS is required and verify the contributor checkout path before adding large binaries.

Depends on: [#33](https://github.com/Afnanksalal/hell-let-loose/issues/33), [#35](https://github.com/Afnanksalal/hell-let-loose/issues/35).
