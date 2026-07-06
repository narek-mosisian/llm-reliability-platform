from typing import cast

from fastapi import APIRouter, Request
from pydantic import BaseModel

from llm_reliability import __version__
from llm_reliability.core.config import Settings

router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


@router.get("", response_model=HealthResponse)
async def health(request: Request) -> HealthResponse:
    settings = cast(Settings, request.app.state.settings)

    return HealthResponse(
        status="ok",
        service=settings.service_name,
        version=__version__,
    )
