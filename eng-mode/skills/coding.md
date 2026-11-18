# Coding

State: Build.

- Follow the surrounding code's conventions. Keep the diff limited to the goal.
- Make retries safe. When work can repeat after a timeout, crash, or retry, define how to detect completion and avoid duplicate effects.
- Read back state before repeating an uncertain write. If the write cannot be retried safely, leave it undone and record why.
