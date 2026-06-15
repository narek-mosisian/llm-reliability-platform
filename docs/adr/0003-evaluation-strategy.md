# ADR 0003: Use golden datasets and CI evaluation gates

## Status

Accepted

## Context

Reliable LLM applications require more than unit tests. The system must verify that generated answers are grounded, cited and resistant to unsupported claims.

RAG quality can regress when changing:

- Prompts
- Chunking strategy
- Embedding model
- Retrieval logic
- Provider or model configuration
- Citation verification
- Refusal behavior

## Decision

Use a golden evaluation dataset and a CI evaluation gate.

The evaluation system should check:

- Answer correctness
- Citation coverage
- Citation validity
- Retrieval precision
- Retrieval recall
- Faithfulness
- Refusal correctness
- Latency
- Estimated cost

The CI evaluation gate should fail when configured score thresholds regress.

## Consequences

Positive:

- Quality becomes measurable
- Regressions can be detected before merge
- Evaluation reports provide reproducible project evidence
- RAG behavior becomes easier to compare across implementation changes
- Citation and refusal behavior become explicit test targets

Negative:

- Dataset maintenance is required
- Metrics cannot capture every qualitative failure mode
- Some manual review remains necessary
- Provider behavior changes can introduce non-determinism

## Alternatives Considered

### Manual testing only

Rejected because manual checks are not reproducible enough for regression detection.

### LLM judge only

Rejected as the only evaluation method because it can be expensive, inconsistent and harder to debug. Deterministic checks should be used first where possible.

### No evaluation gate in CI

Rejected because evaluation is a core reliability requirement for the platform.
