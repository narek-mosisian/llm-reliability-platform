from fastapi import FastAPI

from llm_reliability import __version__
from llm_reliability.api.router import api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="LLM Reliability API",
        version=__version__,
        description="Backend API for the LLM Reliability Platform.",
        docs_url="/docs",  # Swagger documentation
        redoc_url="/redoc",  # ReDoc documentation
        openapi_url="/openapi.json",
    )

    # (Swagger and ReDoc use the same foundation internally: /openapi.json)

    app.include_router(api_router, prefix="/api/v1")

    return app


app = create_app()
