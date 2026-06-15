# ADR 0004: Use OpenTelemetry, Prometheus and Grafana for observability

## Status

Accepted

## Context

The platform needs operational visibility into API behavior, retrieval quality, provider behavior, cost estimates and evaluation trends.

Important signals include:

- Request latency
- Provider latency
- Error rates
- Fallback behavior
- Token usage
- Estimated cost
- Retrieval performance
- Evaluation score trends

## Decision

Use:

- OpenTelemetry for distributed tracing
- Prometheus for metrics
- Grafana for dashboards
- Structured JSON logs through `structlog`

Loki may be added later as an optional centralized logging extension.

## Consequences

Positive:

- Request flows become easier to inspect
- Provider calls and fallback behavior become visible
- Token and cost estimates can be monitored
- Evaluation trends can be shown as operational evidence
- Dashboards can be versioned and documented

Negative:

- Additional services are required
- Metrics and traces require consistent instrumentation
- Dashboard configuration needs maintenance
- Local setup becomes more complex

## Alternatives Considered

### Logs only

Rejected because logs alone do not provide enough visibility into latency distributions, metrics, traces and system trends.

### Hosted-only observability

Rejected for the initial version because self-hosted observability makes the platform behavior and infrastructure more transparent.

### Loki in v1.0

Deferred. Centralized logging is useful, but metrics and traces are more important for the first reliable version.
