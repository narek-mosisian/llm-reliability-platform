# Runbook: Provider Outage

## Purpose

This runbook describes how to respond when the primary LLM provider is unavailable, rate-limited or returning errors.

## Symptoms

Possible indicators:

- Increased provider error rate
- Increased fallback count
- Higher latency
- Failed chat responses
- HTTP 429, 500 or timeout errors from the provider
- Grafana alert or dashboard anomaly

## Immediate Checks

1. Check the API health endpoint.
2. Check the Grafana provider error panel.
3. Check the provider latency panel.
4. Check the fallback count.
5. Check recent logs for provider errors.
6. Check the provider status page manually.

## Mitigation

1. Confirm that the fallback provider is enabled.
2. Switch the primary provider to the fallback provider if needed.
3. Reduce request limits if cost or rate limits are affected.
4. Keep the mock provider available for local demo continuity.
5. Communicate degraded demo behavior if necessary.

## Validation

After mitigation:

- Send a test chat request.
- Confirm that response metadata shows provider and fallback state.
- Confirm that provider errors stop increasing.
- Confirm that latency returns to an acceptable range.

## Evidence

Capture:

- Grafana screenshot
- Error logs
- Example failed request
- Example recovered request
- Configuration change

Store evidence in:

```text
evidence/traces/
evidence/screenshots/
```

## Follow-Up

Create or update an issue with:

- Root cause
- Impact
- Mitigation
- Follow-up tasks
- Eval or test changes if needed
