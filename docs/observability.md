# Observability

## Purpose

This document describes how the LLM Reliability Platform exposes traces, metrics and operational evidence.

The goal is to make system behavior visible and debuggable.

## Observability Stack

The v1.0 observability stack is planned to include:

- OpenTelemetry for traces
- Prometheus for metrics
- Grafana for dashboards
- Structured logs through `structlog`

Optional later extension:

- Loki for centralized logs

## Trace Coverage

Important spans:

```text
http.request
document.upload
document.parse
document.chunk
embedding.generate
rag.retrieve
rag.build_context
gateway.route
provider.call
provider.fallback
citation.verify
eval.run
```

## Metrics

Important metrics:

```text
http_requests_total
http_request_duration_seconds
llm_provider_requests_total
llm_provider_errors_total
llm_provider_latency_seconds
llm_fallbacks_total
llm_tokens_input_total
llm_tokens_output_total
llm_estimated_cost_usd_total
rag_retrieval_latency_seconds
rag_citation_coverage
eval_pass_rate
rate_limit_exceeded_total
```

## Dashboards

Grafana should show:

- Request rate
- Error rate
- p50/p95 latency
- Provider latency
- Provider errors
- Fallback count
- Token usage
- Estimated cost
- Eval score trend
- Rate limit events

## Request IDs and Trace IDs

Every request should have:

- Request ID
- Trace ID
- Provider metadata
- Latency metadata

Trace IDs should be included in API responses where useful for debugging.

## Cost Tracking

The platform estimates LLM cost per request based on:

- Provider
- Model name
- Input tokens
- Output tokens
- Price per 1M input tokens
- Price per 1M output tokens
- Fallback usage
- Retry count

For each answer, the API should expose:

- `input_tokens`
- `output_tokens`
- `total_tokens`
- `estimated_cost_usd`
- `provider`
- `model`
- `fallback_used`

Cost estimates are not billing-grade values. They are operational estimates for debugging, demo safety and budget monitoring.

Provider prices must be reviewed manually whenever model pricing changes.

## Evidence

Operational evidence should be stored in:

```text
evidence/screenshots/
evidence/traces/
evidence/load-tests/
```

Examples:

- Grafana dashboard screenshot
- Trace waterfall screenshot
- Provider fallback event
- Eval score trend
- Load test summary

## Runbooks

Relevant runbooks:

```text
docs/runbooks/provider-outage.md
docs/runbooks/high-latency.md
docs/runbooks/cost-spike.md
docs/runbooks/eval-regression.md
```
