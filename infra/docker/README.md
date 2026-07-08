# Local Docker Platform

This directory documents the local Docker Compose platform for the LLM Reliability Platform.

## Current scope

The local platform includes:

- FastAPI backend service
- Next.js web service
- PostgreSQL with pgvector
- Redis
- OpenTelemetry Collector
- Prometheus
- Grafana

## Local commands

Validate the Compose configuration:

```bash
docker compose config
````

Start the local platform:

```bash
docker compose up --build
```

Stop the local platform:

```bash
docker compose down
```

Remove local volumes:

```bash
docker compose down -v
```

## Local URLs

Web app:

```text
http://localhost:3000
```

API docs:

```text
http://localhost:8000/docs
```

API health endpoint:

```text
http://localhost:8000/api/v1/health
```

Prometheus:

```text
http://localhost:9090
```

Grafana:

```text
http://localhost:3001
```

Default Grafana credentials for local development:

```text
Username: admin
Password: admin
```

## Notes

This setup is for local development and M1 validation only.

It does not include production deployment, Caddy, Cloudflare, Hetzner, CI workflows, RAG endpoints, database migrations or real application metrics yet.

The API metrics endpoint will be added later when Prometheus instrumentation is implemented.
