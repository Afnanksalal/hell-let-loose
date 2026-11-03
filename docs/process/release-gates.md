# Release gates

Gate claims require evidence at the exact commit being released. [Release evidence](../../releases/evidence.json) is machine-checked for complete criteria; humans remain responsible for whether evidence actually proves the claim. CI validates structure and links, not gameplay quality.

| Gate | Required proof | Current status |
| --- | --- | --- |
| G0 Foundation | Navigable knowledge base; user/proposal boundaries; Git/PR/CI process; source provenance; issue board | Repository foundation; remote run recorded before release |
| G1 Prototype | Chosen battle format demonstrated; customization combination; day behavior changes a battle; shared-state proof with at least two clients; one day/night/next-day consequence | Not started |
| G2 Slice | Enjoyable complete 20–30-minute loop; authored episode and narration; representative original FNF-inspired art; save/load and reconnect checks; outsider playtest evidence | Not started |
| G3 Alpha | Committed feature/content scope complete; target six–eight-player behavior measured; aging/memory implementation matches agreed scope; save migration documented; no progression blockers | Not started |
| G4 Beta | Repeated external playtests; performance budget met on named hardware; accessibility/onboarding review; no unresolved critical bugs; distribution/assets verified | Not started |
| G5 Release | Supported platforms/build hashes; backup/recovery and support plan; known issues; final naming and asset/license review; owner go/no-go | Not started |

The gate names organize work; they do not approve an engine, battle format, content count or release date. Record measurable acceptance targets before implementation. No “playable” claim may use only a passing documentation check.

## Required checks and review

All PRs: local Markdown paths valid, source/decision documents present, secret/private-key patterns absent, release manifest valid, checker tests passing. Future code PRs add build, gameplay and multiplayer checks appropriate to the selected engine. Do not fabricate placeholders that always pass as build tests.

Release PRs: version, changelog, manifest, complete gate criteria, evidence links and notes agree. The owner requests the release workflow on main. It verifies the baseline, then creates an immutable tag and GitHub release. Without a release request, no tag or release is published.
