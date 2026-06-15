# Runbook: Cost Spike

## Purpose

This runbook describes how to respond when estimated LLM provider cost increases unexpectedly.

## Symptoms

Possible indicators:

- Estimated cost dashboard spike
- Token usage spike
- Increased request volume
- Increased output length
- Repeated retries
- Abuse of the public demo endpoint

## Immediate Checks

1. Check the token usage dashboard.
2. Check the request count dashboard.
3. Check rate limit events.
4. Check provider retry count.
5. Check recent traffic patterns.
6. Check whether uploads or prompts are unusually large.

## Mitigation

1. Lower per-user request limits.
2. Lower the daily demo request limit.
3. Reduce max output tokens.
4. Disable expensive providers temporarily if needed.
5. Switch to the mock provider if needed.
6. Block abusive traffic if clearly identified.
7. Rotate API keys if abuse or exposure is suspected.

## Validation

Confirm:

- Cost increase stops
- Request volume is controlled
- Rate limits work
- Demo still behaves safely

## Evidence

Capture:

- Cost dashboard
- Token usage dashboard
- Rate limit logs
- Mitigation commit or configuration change

Store in:

```text
evidence/screenshots/
evidence/traces/
```

## Follow-Up

Create follow-up tasks for:

- Better cost alerts
- Stronger abuse prevention
- Improved provider budget controls
- More conservative demo defaults
