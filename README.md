# pipeline-stage-template

**Status:** Initial template  
**Version:** 0.1.0  
**Scope:** Canonical template for DataDiddler lens repositories  
**Layer Position:** Lens template / stage implementation form

This repository defines the standard structure for future DataDiddler lens repos.

It derives from the published `text-pipeline-orchestrator` contract surface and exists to standardize:

- lens repo shape
- CLI expectations
- input/output discipline
- test surfaces
- documentation order

It defines **form only**, not domain behavior.

## Purpose

This template provides the canonical structure for a DataDiddler lens repository.

It exists so future lenses:

- land with the same repo shape
- expose the same documentation surfaces
- conform to the same kernel-facing expectations
- can be inspected and trusted quickly

This repo is a template for one stage implementation inside a larger execution graph.

## Inputs

A lens is invoked by the kernel with explicit CLI arguments.

This template assumes:

- one or more input file paths or input directories
- one output directory
- optional config path(s)

The exact filenames depend on the stage type, but all future lenses should expose their required inputs explicitly in their repo docs.

The minimal example in this template uses:

- `--in`
- `--out-dir`

## Outputs

A lens writes one or more files into the provided output directory.

This template writes:

- `lens_output.ndjson`

Future lenses should document:

- exact output filenames
- whether outputs are required or optional
- whether outputs are schema-bound or pre-schema

## Guarantees

This template guarantees the following shape for future lens repos:

- package structure under `src/`
- one minimal runnable lens entrypoint
- top-level README in canonical order
- docs for interface, expected inputs, expected outputs
- minimal example surfaces
- minimal tests

The included sample implementation:

- parses CLI arguments
- validates input path existence
- creates output directory
- writes at least one output file
- returns `0` on success

## Non-guarantees

This template does **not** guarantee:

- domain logic
- semantic correctness
- schema authority
- orchestration behavior
- policy behavior
- rendering behavior
- downstream consumer behavior

It is not a reference implementation of a real lens stage.
It is a structural template.

## Quick run

From the repo root:

```bash
python -m lens_template.lens --in examples/sample_in/input.txt --out-dir examples/sample_out
```

Expected result:

```
examples/sample_out/lens_output.ndjson
```

Contract test

```

Minimal checks:

python -m pytest

These tests verify:

package import works
expected files exist
template structure is present
```

What this is not

````

This repo is not:

the kernel
a schema authority
a domain lens
a policy layer
a renderer
a consumer
a complete stage implementation for production use

It implements one stage shape inside a larger execution graph and defines the canonical form future lenses should inherit.


---

# `pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "datadiddler-lens-template"
version = "0.1.0"
description = "Canonical template for DataDiddler lens repositories."
readme = "README.md"
requires-python = ">=3.10"
authors = [
  { name = "MettleForgeLab" }
]
license = { text = "Proprietary or project-defined" }
dependencies = []

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
````
