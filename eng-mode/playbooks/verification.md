# Verification

State: Test. Nodes: `Verify actual behavior`, `Evidence`.

1. Run every required acceptance check on the current artifact in the relevant environment. Read [validation](../skills/validation.md).
2. Exercise the behavior the goal claims. Run the regression check, the nearby behavior checks, and the affected project checks. Read [testing](../skills/testing.md).
3. Run the affected checks again after the last relevant change.
4. Reproduce decisive worker evidence yourself. A worker's summary is not verification.
5. Record every acceptance check in the evidence table. Read [evidence collection](../skills/evidence-collection.md). Mark a check that could not run as not run, and record why.

For documentation, check the instructions, paths, examples, and claims against the real artifact. For a skill, check discovery and invocation, then exercise representative tasks. Text validation alone does not prove agent behavior.
