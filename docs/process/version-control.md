# Version control

Main holds reviewed work. Use short-lived issue-linked branches and squash merge pull requests. Delete merged topic branches. Revert through a new PR rather than rewriting published history.

Main requires passing Repository checks against current main, resolved review conversations and linear history. Force pushes and deletion are blocked. No bypass actor is configured. External approvals are not required while there is one maintainer; the PR and CI record still applies.

## Versions

VERSION identifies a candidate baseline. Use major.minor.patch numbers, with release notes describing compatibility before 1.0. Version 0.1.0 establishes repository structure, not a playable game. Tags use `v` followed by VERSION and identify a commit on main. Published version tags cannot be moved or deleted.

The [release procedure](releasing.md) separates editing a version file from publishing a release. Runtime and save-format compatibility will be specified when those interfaces exist.

## Repository contents

Commit editable source and required project configuration. Exclude engine caches, local settings, credentials and build output. Choose asset-specific large-file handling with the production pipeline.

The repository is public and source-available under [LICENSE](../../LICENSE). Redistribution and sale require permission. Third-party code and assets retain their own identified terms.
