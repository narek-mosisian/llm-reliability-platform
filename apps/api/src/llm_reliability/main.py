from fastapi import FastAPI

from llm_reliability import __version__
from llm_reliability.api.router import api_router
from llm_reliability.core.config import Settings, get_settings
from llm_reliability.core.errors import register_exception_handlers
from llm_reliability.core.logging import configure_logging


def create_app(settings: Settings | None = None) -> FastAPI:
    resolved_settings = settings or get_settings()

    configure_logging(resolved_settings)

    app = FastAPI(
        title=resolved_settings.api_title,
        version=__version__,
        description="Backend API for the LLM Reliability Platform.",
        docs_url="/docs",  # Swagger documentation
        redoc_url="/redoc",  # ReDoc documentation
        openapi_url="/openapi.json",
        debug=resolved_settings.debug,
    )

    # (Swagger and ReDoc use the same foundation internally: /openapi.json)

    app.state.settings = resolved_settings

    register_exception_handlers(app)
    app.include_router(api_router, prefix="/api/v1")

    return app


app = create_app()
