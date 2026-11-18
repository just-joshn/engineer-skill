# Acceptance criteria

State: Plan.

- Write each check as an observable result: an output, a file's bytes, a test that fails before and passes after, or a user-visible behavior.
- Define the expected result before any run. Derive it from the requirement, not from the implementation.
- Include the relevant failure and boundary cases.
- For incorrect behavior, one check is that the regression check fails on the unchanged artifact. A fix without that failure on record is not verified.
- For an assessment or a question, each finding or answer is supported by evidence. A defect in the assessed artifact is a finding, not a failed check.
- Never weaken a check to obtain a pass.
