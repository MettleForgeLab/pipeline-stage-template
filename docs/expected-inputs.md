# Expected Inputs

This template documents input expectations for a generic DataDiddler lens.

## Template-level inputs

The sample template lens expects:

- one input file via `--in`
- one output directory via `--out-dir`

## Kernel-aligned stage reality

Actual DataDiddler lenses may consume files such as:

- `documents.ndjson`
- `text_artifacts.ndjson`
- `triage.ndjson`
- `entities.ndjson`
- `events.ndjson`
- `claims.ndjson`
- `edges.ndjson`
- `threads.ndjson`

Which files apply depends on the stage type.

## Stage examples

### Separator-like lens

Common inputs:

- `documents.ndjson`
- `text_artifacts.ndjson`

### Tagger-like lens

Common inputs:

- `triage.ndjson`
- `documents.ndjson`
- `text_artifacts.ndjson`

### Packager-adjacent lens

Common inputs:

- `documents.ndjson`
- `triage.ndjson`
- `entities.ndjson`
- `events.ndjson`
- `claims.ndjson`
- `edges.ndjson`
- `threads.ndjson` (if expected by the current contract shape)

## Rule

Every future lens repo should explicitly declare:

- which input files it requires
- which are optional
- whether those inputs are pre-schema or schema-bound
