# Runbook: High Latency

## Purpose

This runbook describes how to investigate and mitigate high latency in the platform.

## Symptoms

Possible indicators:

- p95 latency above target
- Slow chat responses
- Slow document upload
- Slow retrieval
- Slow provider calls
- Timeout errors

## Immediate Checks

### Public or local checks

These checks can be performed by contributors without production server access:

1. Reproduce the issue locally with Docker Compose.
2. Check API response times from the local environment.
3. Check whether slow requests are related to document size, retrieval or provider calls.
4. Run available smoke tests.
5. Inspect local container resource usage with `docker stats`.

### Operator-only checks

These checks require access to the production server or observability dashboards:

1. Check Grafana p50 and p95 latency panels.
2. Compare API latency and provider latency.
3. Check database query latency.
4. Check retrieval latency.
5. Check provider fallback events.
6. Check server CPU, memory and disk usage.

## Possible Causes

- LLM provider slowdown
- Large uploaded documents
- Slow embedding generation
- Inefficient vector search
- Database resource pressure
- Redis or network issues
- Server resource exhaustion

## Mitigation

1. Reduce retrieval limit temporarily.
2. Enforce stricter upload limits.
3. Increase provider timeout only if justified.
4. Enable fallback provider if provider latency is high.
5. Restart unhealthy services if necessary.
6. Scale server resources only after confirming the bottleneck.

## Validation

Confirm:

- p95 latency decreases
- Error rate remains stable
- Eval quality does not regress
- Fallback behavior is expected

## Evidence

Capture:

- Latency dashboard screenshot
- Trace waterfall
- Slow request example
- Mitigation result

Store evidence in:

```text
evidence/traces/
evidence/load-tests/
evidence/screenshots/
```
