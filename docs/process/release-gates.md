# Release gates

Each release candidate needs evidence tied to the commit being released. [Gate definitions](../../releases/gates.json) list required criteria; [current evidence](../../releases/evidence.json) records the baseline under review.

| Gate | Required evidence | Status |
| --- | --- | --- |
| G0 Foundation | Repository structure, design decisions, contribution process, passing checks and project tracking | Being finalized |
| G1 Prototype | Battle format demonstrated, customization combination, behavior-derived move, two-client shared state and connected phase loop | Not started |
| G2 Slice | Complete session, authored episode and narration, representative original art, save/load and reconnect, external playtest | Not started |
| G3 Alpha | Agreed feature scope, target party scale, aging scope, save migration and no progression blockers | Not started |
| G4 Beta | Repeated external playtests, measured performance, accessibility/onboarding review, no critical bugs and verified distribution assets | Not started |
| G5 Release | Build hashes/platforms, recovery/support, known issues, naming/rights review and owner go/no-go | Not started |

Repository CI checks documentation. It does not prove gameplay quality or a functioning build. Add actual build and runtime tests with engine integration. Define measurable performance and playtest targets before those gates are evaluated.

Release PRs must agree on version, changelog, notes and gate criteria. Every passing criterion needs evidence. Pending or failed criteria block publication. The owner requests the Release workflow on main after review.
