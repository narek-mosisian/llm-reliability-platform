# Runbook: Evaluation Regression

## Purpose

This runbook describes how to respond when evaluation quality drops below the required threshold.

## Symptoms

Possible indicators:

- CI eval gate fails
- Pass rate decreases
- Citation coverage decreases
- Refusal correctness decreases
- Forbidden claims appear
- Retrieval quality drops

## Immediate Checks

1. Open the failed CI run.
2. Download or inspect the eval report.
3. Identify failed cases.
4. Compare the current report with the previous passing report.
5. Check recent changes to prompts, chunking, retrieval, embeddings or provider settings.

## Common Causes

- Prompt regression
- Changed chunking behavior
- Retrieval ranking issue
- Embedding model change
- Provider or model behavior change
- Dataset expectation mismatch
- Citation verification bug

## Mitigation

1. Reproduce the failed eval locally.
2. Inspect retrieved chunks for failed cases.
3. Check whether the expected source is retrievable.
4. Fix retrieval, prompt or citation logic.
5. Update the dataset only if the dataset expectation is clearly wrong.
6. Rerun all evals.

## Validation

The regression is resolved when:

- CI eval gate passes
- Failed cases are fixed
- No new critical regressions appear
- The updated report is stored as evidence

## Evidence

Store:

- Failed report
- Fixed report
- PR link
- Explanation of root cause

Use:

```text
evidence/eval-reports/
```
