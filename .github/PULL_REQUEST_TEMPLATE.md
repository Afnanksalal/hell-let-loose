## Change and reason

Describe the resulting behavior or design decision. Link the issue with `Closes #...` when appropriate.

## Authority and scope

- [ ] Confirmed direction and new proposals remain distinct.
- [ ] Relevant topic, decision register and changelog updated where needed.
- [ ] Acceptance criteria met; dependencies and open questions documented.

## Validation

Record commands/results and links to relevant screenshots, playtests or builds. For documentation changes, repository checks are sufficient.

- [ ] `python scripts/check_repository.py`
- [ ] `python -m unittest discover -s tests -v`
- [ ] Release gate evidence updated if this is a release PR.

## Risks or limitations

State material limitations and any rollback/revert considerations.
