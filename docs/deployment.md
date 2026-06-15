# Deployment

## Purpose

This document describes the planned production deployment for the LLM Reliability Platform.

The first deployment target is:

```text
Hetzner VPS + Cloudflare DNS/TLS + Docker Compose + Caddy
```

## Deployment Goals

The deployment should demonstrate:

- Real public hosting
- HTTPS
- Reverse proxy configuration
- Containerized services
- Production environment variables
- Basic backup and restore process
- Smoke tests
- Operational documentation

## Planned Endpoint Layout

The final deployment is expected to expose the following endpoint structure. The concrete domain will be configured during the production deployment milestone.

| Purpose | Planned endpoint |
|---|---|
| Landing page | `https://llm-reliability.<domain>` |
| Demo | `https://demo.llm-reliability.<domain>` |
| API docs | `https://api.llm-reliability.<domain>/docs` |
| Evidence | `https://llm-reliability.<domain>/evidence` |

## Services

The production Compose setup should include:

- `web`
- `api`
- `postgres`
- `redis`
- `caddy`
- `prometheus`
- `grafana`
- `otel-collector`

## Environment Variables

Production secrets must not be committed.

Production configuration should use:

- GitHub environment secrets
- Server-side `.env` files
- Restricted file permissions
- Rotation procedure for provider keys

## Deployment Workflow

Planned deployment flow:

```text
Push to main
  |
  v
GitHub Actions workflow
  |
  v
SSH into server
  |
  v
Pull latest changes or image
  |
  v
Run Docker Compose update
  |
  v
Run smoke tests
  |
  v
Capture deployment evidence
```

## Smoke Tests

After deployment, verify:

- Web app is reachable
- API health endpoint returns OK
- API docs are reachable
- Grafana is reachable
- Prometheus target status is healthy
- A demo RAG request works
- Logs do not show startup errors

## Rollback

Rollback steps are documented in:

```text
docs/runbooks/rollback.md
```

## Backup and Restore

Backup and restore steps are documented in:

```text
docs/runbooks/backup-restore.md
```

## Non-Goals for v1.0

The first deployment does not include:

- Kubernetes
- Stripe billing
- Social login
- Multi-tenant SaaS accounts
- Complex admin roles
