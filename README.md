# Engineering mode

Engineering mode is an opinionated, instruction-driven engineering workflow for any agent harness that can read instructions. Its canonical entry point is `eng-mode/SKILL.md`. `/eng-mode` is a convenience command where the host supports it.

You supply the desired result and constraints. The agent takes responsibility for choosing and carrying out the engineering work. It establishes acceptance checks, selects a playbook, applies relevant principles, delegates bounded work, verifies the outcome, and reports evidence.

## Structured ownership

The coordinating agent owns the whole result, including work produced by other agents. Delegation requires a clear contract and separate outputs. Worker completion does not establish overall completion.

The workflow prefers small, complete changes, explicit boundaries, root-cause fixes, and behavior checks. It rejects speculative abstractions, shared concurrent writes, unsupported success claims, and delivery beyond the user's authority.

Small tasks use a short path. Independent work can run in parallel. Uncertainty calls for investigation rather than a larger implementation plan.

## Explicit evidence

The workflow separates creating an artifact from demonstrating that it meets the goal.

A correctable failure returns the agent to investigation and method selection. A blocked or inconclusive result requires a report of limits and remaining work. A verified result proceeds only to the authorized endpoint.

A merge requires separate shipping gates and confirmation of the actual remote state. Passing local checks does not authorize a merge.

## Scope and limits

The standalone `eng-mode/` directory uses the Agent Skills format. It contains the complete workflow, principles, playbooks, delegation contract, and task-record template. It has no runtime dependency on Node, Pi, a model provider, or a particular worker tool.

Use the same directory with Claude Code CLI, Codex CLI, Pi, OpenCode, or another compatible host. An agent without native skill discovery can read `eng-mode/SKILL.md` directly. Native installation and command syntax remain host-specific.

The repository also contains an optional Pi adapter. It preserves multiline requests, indentation, and quotes for Pi's `/eng-mode` shortcut. It is not required by the standalone skill or other harnesses.

These instructions do not add tools, enforce permissions in code, or guarantee model compliance. The intended benefit is a working discipline, not a measured productivity claim.

- [Install and use engineering mode](docs/usage.md).
- [Read the workflow and engineering principles](eng-mode/SKILL.md).
- [Use the optional Pi adapter](docs/pi.md).
- [Run validation and behavior scenarios](evals/README.md).
