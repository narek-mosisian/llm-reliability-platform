from fastapi import APIRouter

from llm_reliability.api.routes import health

api_router = APIRouter()

api_router.include_router(health.router, prefix="/health", tags=["health"])
