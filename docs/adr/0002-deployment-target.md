# ADR 0002: Use Hetzner, Cloudflare, Docker Compose and Caddy for deployment

## Status

Accepted

## Context

The project needs a realistic live deployment that is affordable, understandable and maintainable for a small project setup.

The deployment should demonstrate:

- Public hosting
- HTTPS
- Reverse proxying
- Containerized services
- Environment separation
- Operational documentation
- Smoke tests
- Backup and rollback procedures

## Decision

Use:

- Hetzner VPS for compute
- Cloudflare for DNS and TLS-related configuration
- Docker Compose for service orchestration
- Caddy as reverse proxy
- GitHub Actions for deployment automation

## Consequences

Positive:

- Affordable infrastructure setup
- Transparent infrastructure and deployment model
- Easier to operate than Kubernetes for v1.0
- Suitable for a public demo deployment
- Compatible with PostgreSQL, Redis, Prometheus, Grafana and OpenTelemetry Collector

Negative:

- Server operations and hardening remain project responsibilities
- Horizontal scaling is limited compared to Kubernetes-based deployments
- Deployment reliability depends on careful server configuration and backup procedures

## Alternatives Considered

### Kubernetes

Rejected for v1.0 because it would increase operational complexity and distract from the core LLM reliability features.

### Serverless-only deployment

Rejected because it would make PostgreSQL, Grafana, Prometheus, OpenTelemetry and provider gateway operations less transparent.

### Managed PaaS

Rejected for v1.0 because it hides infrastructure and deployment details that are important for this platform.
