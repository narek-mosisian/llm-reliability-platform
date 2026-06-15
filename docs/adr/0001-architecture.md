# ADR 0001: Use a modular FastAPI and Next.js architecture

## Status

Accepted

## Context

The project requires a modular architecture that separates the user interface, API layer, document ingestion, retrieval, provider access, evaluation and observability concerns.

A simple chatbot implementation would combine too many responsibilities and make it harder to test, operate and extend the system.

The architecture should support:

- A web user interface
- A backend API layer
- Document ingestion
- Retrieval-augmented generation
- LLM provider abstraction
- Evaluation workflows
- Observability
- Deployment automation

## Decision

Use a modular architecture with:

- FastAPI for the backend API
- Next.js for the frontend application
- PostgreSQL with pgvector for relational data and vector search
- Redis for rate limiting and lightweight runtime state
- LangChain for selected RAG primitives
- LangGraph for bounded workflow orchestration
- OpenTelemetry, Prometheus and Grafana for observability
- Docker Compose for the initial local and production-like deployment model

## Consequences

Positive:

- Clear separation of concerns
- Clear operational and architectural boundaries
- Easier testing and documentation
- More explicit reliability and observability structure
- Extensible foundation for later hybrid search and Semantic Web features

Negative:

- More setup than a minimal chatbot application
- More documentation and configuration are required
- More components need to be maintained

## Alternatives Considered

### Single Next.js full-stack application

Rejected because it would combine too many responsibilities in one application layer.

### Streamlit demo

Rejected for the main application because it is better suited for fast prototypes and internal demos than for a production-like platform with a public frontend, API integration, evidence pages and deployment documentation.

### Kubernetes-first deployment

Rejected for v1.0 because it adds operational complexity before the core system behavior is implemented and evaluated.
