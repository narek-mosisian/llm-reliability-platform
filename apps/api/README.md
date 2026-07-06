# LLM Reliability API

Backend API for the LLM Reliability Platform.

This service will provide the FastAPI backend for document ingestion, RAG, LLM gateway routing, evaluations, observability and operational endpoints.

## Current scope

This initial skeleton includes:

- FastAPI application factory
- Versioned API router
- Health endpoint
- Basic test coverage for the health endpoint
- Basic test coverage for the OpenAPI schema

## Local development

Install dependencies:

```bash
uv sync
```

Run tests:

```bash
uv run pytest
```

Run the API locally:

```bash
uv run uvicorn llm_reliability.main:app --reload
```

Open the API docs:

```text
http://localhost:8000/docs
```

Open the OpenAPI schema:

```text
http://localhost:8000/openapi.json
```

Health endpoint:

```text
http://localhost:8000/api/v1/health
```

## Planned next steps

The next implementation steps will add:

- Backend configuration loading
- Structured logging
- Error handling
- Docker Compose integration
- PostgreSQL
- Redis
- OpenTelemetry Collector
- Prometheus
- Grafana
- Local smoke tests
- CI workflows
