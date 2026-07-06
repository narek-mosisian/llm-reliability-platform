from fastapi import APIRouter
from pydantic import BaseModel

from llm_reliability import __version__

router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


@router.get("", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        service="llm-reliability-api",
        version=__version__,
    )
