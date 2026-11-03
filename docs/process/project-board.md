# Project workflow

The [development board](https://github.com/users/Afnanksalal/projects/3) tracks repository issues. Each issue holds the outcome, acceptance criteria and dependencies. [Backlog data](../../planning/backlog.json) records the initial setup; live status belongs on GitHub.

| Status | Meaning | Exit condition |
| --- | --- | --- |
| Todo | Work awaiting selection | Scope and dependencies understood |
| In Progress | Active design or implementation | Acceptance criteria met and review ready |
| Done | Accepted work | PR merged or decision recorded |

Use the blocked label with a specific unblock condition. Use needs-decision when implementation depends on an unsettled choice. Keep no more than two active tasks per person.

Priority identifies blocking, next and later work. Area identifies the subsystem. Gate identifies the required milestone evidence. Milestones group acceptance batches without promising dates.

During triage, split oversized tasks, resolve stale blockers and attach observations or build evidence. Closing a milestone does not automatically pass a release gate. Add new issues to the Project through GitHub or the CLI; account-wide credentials are not stored in Actions.
