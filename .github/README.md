# GitHub configuration

The Checks workflow validates Markdown and local documentation links. It does not claim to build or test the game before runtime integration.

Main requires a pull request, passing Repository checks, linear history and resolved review conversations. Version tags cannot be rewritten or deleted. The rulesets directory records those settings for reproducibility.

Issue templates capture tasks, design decisions and defects. The pull request template asks for scope and validation evidence. Workflow action updates are maintained manually.

The Release workflow is manually requested by the repository owner on main. It validates versioned evidence before publishing. Higher gates require actual build and playtest records.
