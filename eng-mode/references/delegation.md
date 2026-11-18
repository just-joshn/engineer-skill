# Delegate without transferring responsibility

Delegate only when a bounded task has a clear deliverable and can proceed independently. Do not delegate an unresolved interface decision as parallel implementation.

## Prepare a worker contract

Give each worker:

- The goal and relevant user constraints.
- Its exact question or deliverable and acceptance checks.
- Input paths, context, assumptions, and dependency boundaries.
- Its owner identifier and allowed files or isolated worktree.
- Forbidden actions and the authorized endpoint.
- The commands or interactions that can prove completion.
- A required report with changed artifacts, observed evidence, limitations, and unresolved questions.

Workers do not inherit your conversation. Pass the needed context explicitly. Give file pointers for large artifacts. Use the host's supported worker mechanism. Do not assume a particular provider, model, or worker tool is installed.

Default workers to local output only. They must not publish, merge, deploy, delete shared data, or delegate further unless their contract explicitly permits it.

## Separate work

1. Define shared interfaces and integration order before workers edit.
2. Give each writer a separate worktree or non-overlapping files.
3. Give independent reviewers distinct risk questions and the same acceptance contract.
4. Track dependencies. Do not start a worker whose inputs are still changing.
5. If a worker fails, inspect its partial output before retrying. Do not duplicate uncertain external actions.

## Integrate as the owner

1. Inspect every proposed change against the contract and the user's goal.
2. Reject scope expansion, unsupported claims, and workarounds that hide the cause.
3. Reproduce decisive worker evidence. Run acceptance checks on the combined artifact.
4. Resolve disagreements with an experiment or direct inspection. A majority vote is not evidence.
5. Update the task record and deliver one coherent result.

A worker may finish its assignment while the overall task remains blocked. Report those states separately.
