# Project board

The GitHub Project linked from the root README is the live task tracker. Repository issues hold the full task and acceptance criteria; the Project provides status, priority, area and gate views. The seed data in [project backlog](../../planning/backlog.json) records the initial setup, not a second live status tracker.

## Status flow

| Status | Meaning | Exit condition |
| --- | --- | --- |
| Todo | Backlog or triage | Scope, acceptance criteria and dependencies clear |
| In Progress | Actively being designed or implemented | PR/evidence ready and acceptance criteria checked |
| Done | Accepted work | Linked PR merged or decision outcome documented |

Use `blocked` for a dependency that prevents progress. Record the blocker and unblock condition in the issue. Keep at most two In Progress tasks per person. Use `needs-decision` when owner direction is required rather than pretending a proposal is approved.

## Fields

- Priority: P0 blocking, P1 next, P2 later.
- Area: Governance, Design, Art, Narrative, Gameplay, Multiplayer.
- Gate: G0 Foundation, G1 Prototype, G2 Slice, G3 Alpha, G4 Beta, G5 Release.
- Milestone: acceptance batch, with no invented delivery dates.

Keep new tasks in Todo until ready. A milestone being closed does not automatically pass a release gate. Add new issues to the Project through the issue sidebar or CLI; no broad account token is stored in Actions to auto-add items.

Weekly or before a work session: triage new issues, clear stale blockers, narrow oversized tasks and attach evidence. Don't manufacture progress updates for unchanged work.
