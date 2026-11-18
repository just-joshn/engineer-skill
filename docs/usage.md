# Install and use engineering mode

## Use any agent that can read files

Give the agent this instruction, with the actual checkout path:

```text
Read /absolute/path/to/engineer-skill/eng-mode/SKILL.md and follow it for this task.
Resolve its bundled references relative to that directory.

Goal: fix duplicate submissions.
Constraints: preserve the public API and add a regression test.
Authorized endpoint: local changes and evidence only. Do not publish or merge.
```

This method does not need native skill discovery, a slash command, a package manager, or a harness extension. If the agent cannot read local files, provide the entry file and the supporting files it needs through the host's attachment mechanism.

## Install for native discovery

Copy the entire `eng-mode/` directory into your host's supported skill directory. Keep the playbooks, references, and template with `SKILL.md`.

Alternatively, use the [Skills installer](https://github.com/vercel-labs/skills) from the target project, not this source repository:

```sh
npx skills@latest add /absolute/path/to/engineer-skill/eng-mode --skill eng-mode --agent claude-code codex opencode pi --copy
```

Remove agents you do not use. The installer selects each host's skill directory. This installs only the standalone skill, not the optional Pi adapter.

Use the host's native skill selector or ask it to load `eng-mode`. Do not assume that `/eng-mode`, `$eng-mode`, and `/skill:eng-mode` are interchangeable across hosts.

For Pi's optional `/eng-mode` shortcut, use [the Pi adapter guide](pi.md).

## Control the scope

Supply the desired result, constraints, and authorized endpoint. Let the agent choose the playbook and tools.

To request the workflow for the session, tell the agent:

```text
Read the eng-mode skill and keep engineering mode active for this session.
```

Then supply the task. To disable the workflow, say:

```text
Turn engineering mode off.
```

Session persistence depends on the host and model. Repeat the invocation after a context reset if the host does not retain it.

## Work within the host's capabilities

When workers are unavailable, the agent performs the work locally. When an acceptance check cannot run, the agent reports the evidence gap. Do not install extra infrastructure merely to follow this workflow.

The portable skill does not grant permissions or add execution, network, browser, device, or worker tools.

## Validate changes

From this repository, run:

```sh
python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

For behavioral verification, run the relevant [scenarios](../evals/README.md) in the target harness. Record the actual host and model. Installer compatibility and structural tests do not establish behavioral compliance.
