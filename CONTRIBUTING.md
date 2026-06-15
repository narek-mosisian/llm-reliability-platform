# Contributing

## Project Status

This project is in early development. The initial goal is to build a production-grade LLMOps platform for reliable RAG-based AI assistants with evaluations, observability, fallback routing, cost controls and live deployment.

This project is primarily maintained by Narek Mosisian. Feedback, suggestions and pull requests are welcome, but all changes are reviewed before they are merged.

## Branch Naming

Use focused branches:

```text
chore/repository-foundation
docs/initial-readme
infra/docker-compose-skeleton
feature/document-ingestion
feature/rag-core
ci/eval-gate
fix/rate-limit-error
```

## Commit Messages

Use Conventional Commits in imperative form:

```text
feat: add document ingestion endpoint
fix: handle empty PDF uploads
docs: document evaluation strategy
chore: configure pre-commit hooks
ci: add API test workflow
infra: add Docker Compose skeleton
```

## Local Setup

Install project tooling:

```bash
brew install pre-commit just uv pnpm
```

Install Git hooks once per clone:

```bash
pre-commit install
```

Run all hooks manually:

```bash
pre-commit run --all-files
```

`pre-commit install` registers local Git hooks in `.git/hooks/`. This step is required for every local clone because Git hooks are not installed automatically when a repository is cloned.

## Pull Request Requirements

Every pull request should include:

* Clear summary
* Linked issue, when applicable
* Implementation notes
* Test evidence
* Security impact
* Deployment impact
* Screenshots or reports when applicable

## Quality Expectations

Before opening a pull request, run:

```bash
pre-commit run --all-files
```

Later project phases may also require:

```bash
just api-test
just api-lint
just web-lint
just web-build
just eval
```

## Documentation Expectations

Architecture, reliability and operational decisions should be documented in:

```text
docs/
docs/adr/
docs/runbooks/
```

Important engineering decisions should receive an ADR.
