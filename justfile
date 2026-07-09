set shell := ["bash", "-cu"]

setup:
  cp -n .env.example .env || true
  cd apps/api && uv sync
  cd apps/web && pnpm install

dev:
  docker compose up --build

down:
  docker compose down

logs:
  docker compose logs -f --tail=200

compose-config:
  docker compose config

smoke:
  ./scripts/smoke-local.sh

api-test:
  cd apps/api && uv run pytest

api-lint:
  cd apps/api && uv run ruff check src tests && uv run mypy src

api-format:
  cd apps/api && uv run ruff format src tests

web-lint:
  cd apps/web && pnpm lint

web-build:
  cd apps/web && pnpm build

format:
  cd apps/api && uv run ruff format src tests

eval:
  cd apps/api && uv run python -m llm_reliability.scripts.run_evals
