# Use the optional Pi adapter

The standalone skill does not need this adapter. Use it when you want Pi's `/eng-mode` shortcut with lossless multiline input.

## Try the package

1. Review `extensions/eng-mode.ts`. Pi extensions run with the host process's permissions.
2. From this repository, start Pi with the package loaded:

```sh
pi -e .
```

3. Supply the task:

```text
/eng-mode Fix duplicate submissions. Preserve the public API. Add a regression test. Do not publish or merge.
```

The input adapter forwards the request to Pi's native skill command before prompt-template argument parsing. Keep the package's extension enabled.

Without the adapter, use the native command after installing the standalone skill:

```text
/skill:eng-mode Investigate why startup hangs. Report evidence. Do not change production.
```

## Register the local package

From this repository, run:

```sh
pi install "$(pwd)"
```

Start Pi, or run `/reload` in an active session. Keep the checkout at that path. A local package loads its files without copying them.

If another extension owns `/eng-mode`, use `/skill:eng-mode` to avoid the command conflict.

## Validate the adapter

With Node 24 or newer, run:

```sh
node --test scripts/test_command.ts
```

For the portable workflow and other harnesses, use [the general installation guide](usage.md).
