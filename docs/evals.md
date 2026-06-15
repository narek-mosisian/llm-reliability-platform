# Evaluation Strategy

## Purpose

This document describes how the project evaluates RAG answer quality, citation reliability and regression risk.

The goal is to prove that the system is not only generating answers, but generating grounded and testable answers.

## Evaluation Types

### Offline Evals

Offline evals run on a fixed golden dataset before changes are merged.

They check:

- Answer correctness
- Citation coverage
- Citation validity
- Retrieval precision
- Retrieval recall
- Faithfulness
- Refusal correctness
- Latency
- Estimated cost

### CI Eval Gate

The CI eval gate should fail when quality drops below defined thresholds.

Example checks:

```text
answer_correctness >= 0.80
citation_coverage >= 0.90
refusal_correctness >= 0.95
```

### Online Evaluation

Online evaluation may be added later for live demo traffic.

Planned online evaluation signals include:

- User feedback
- Error rate
- Fallback rate
- Latency distribution
- Cost per answer
- Refusal rate

## Golden Dataset

The golden dataset lives in:

```text
evals/datasets/golden-rag-qa.jsonl
```

Each case should include:

- ID
- Question
- Expected answer fragments
- Required chunk IDs
- Forbidden claims
- Refusal expectation
- Category
- Difficulty

## Example Case

```json
{
  "id": "case_001",
  "question": "What is Acme's default data retention period?",
  "expected_answer_contains": ["90 days"],
  "required_chunk_ids": ["doc:security-policy:pos:12"],
  "forbidden_claims": ["180 days", "one year"],
  "should_refuse": false,
  "category": "simple_lookup",
  "difficulty": "easy"
}
```

## Metrics

Planned metrics:

```text
answer_correctness
citation_coverage
citation_validity
retrieval_precision
retrieval_recall
faithfulness
refusal_correctness
p95_latency
estimated_cost_per_answer
```

## Reports

Evaluation reports should be written to:

```text
evals/reports/
evidence/eval-reports/
```

Report formats:

- JSON
- Markdown

## Evidence

Selected reports should be linked from:

```text
README.md
docs/evals.md
evidence/
```

## Failure Handling

When an eval regression occurs:

1. Identify failed cases.
2. Compare retrieved chunks.
3. Check prompt changes.
4. Check model/provider changes.
5. Check chunking or embedding changes.
6. Fix or update the dataset only if the previous expectation was wrong.

The operational process is documented in:

```text
docs/runbooks/eval-regression.md
```
