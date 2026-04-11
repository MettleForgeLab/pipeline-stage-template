# Expected Outputs

This template documents output expectations for a generic DataDiddler lens.

## Template-level outputs

The sample template lens writes:

- `lens_output.ndjson`

This file exists only to demonstrate the shape of a lens output.

## Kernel-aligned stage reality

Actual DataDiddler lenses may write files such as:

- `triage.ndjson`
- `entities.ndjson`
- `events.ndjson`
- `claims.ndjson`
- `edges.ndjson`
- `threads.ndjson`

Which outputs apply depends on the stage type.

## Output rules

A future lens should document:

- exact filenames produced
- whether outputs are required or optional
- whether outputs may be empty
- whether outputs are pre-schema or schema-bound

## Boundary

A lens does not emit:

- `run_manifest.json`
- `stage_status.ndjson`

Those are kernel truth surfaces.
