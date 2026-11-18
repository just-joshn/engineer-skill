# Testing

State: Test.

- Test behavior, not implementation. Assert outputs and effects that a caller can observe.
- Derive expected values from the requirement. Reject tests that repeat the implementation or only confirm an internal helper was called.
- A passing test proves a bug fix only if the same test failed on the unchanged artifact.
