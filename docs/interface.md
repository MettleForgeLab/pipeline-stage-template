# Interface

This document describes how the DataDiddler kernel invokes lenses.

## Invocation model

A lens is executed as a stage-local tool with explicit CLI arguments.

The kernel is responsible for:

- orchestration
- stage order
- tool mapping
- schema authority
- run truth surfaces

A lens is responsible for:

- accepting expected inputs
- writing expected outputs
- returning an honest exit code

## CLI expectations

A lens should expose a small, explicit CLI.

At minimum, a lens should accept:

- one or more input paths
- one output directory

Optional:

- config path(s)
- stage-specific flags

This template uses:

- `--in`
- `--out-dir`

## Return codes

Expected behavior:

- `0` on success
- non-zero on failure

A lens should not silently claim success if required outputs were not produced.

## File IO expectations

A lens should:

- read only the files it was asked to read
- write outputs only to the provided output directory
- not assume orchestration state
- not assume schema authority
- not write run manifests or stage status

Those belong to the kernel.

## Boundary

A lens:

- does not define orchestration
- does not define schema authority
- does not define policy
- does not define downstream rendering or consumer logic

It implements one stage inside a larger execution graph.
