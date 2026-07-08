FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim
# uses a ready-made base image with:
# Python 3.12
# uv package manager
# Debian Bookworm (slim)
# (a base image is simply the image on which your own image is built)

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
# Python should not write .pyc cache files
ENV PYTHONUNBUFFERED=1
# Python should output logs immediately instead of buffering them, so that they can be viewed directly via Docker
ENV UV_COMPILE_BYTECODE=1
# uv should precompile Python bytecode to make the app's startup slightly faster
ENV UV_LINK_MODE=copy
# uv should copy dependencies instead of linking them, as this is
# often more robust in Docker, since symlinks and hard links can sometimes cause issues
ENV PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml uv.lock README.md ./
COPY src ./src

RUN uv sync --frozen --no-dev
# installs the Python dependencies:
# * uv sync: synchronizes the virtual environment with pyproject.toml and uv.lock
# * --frozen: the lock file must not be changed (exactly the versions from uv.lock are used)
# * --no-dev: does not install development dependencies (e.g. no test/lint tools if they are marked as dev dependencies)

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "llm_reliability.main:app", "--host", "0.0.0.0", "--port", "8000"]
# start FastAPI with Uvicorn
# --host 0.0.0.0: the API listens on all network addresses in the container (with only localhost it would probably not be reachable from outside)
# (accepts connections from outside to the container)
