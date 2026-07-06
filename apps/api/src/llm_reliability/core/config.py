from functools import lru_cache
from typing import Literal

from pydantic import Field

# to set defaults and alias names for fields
from pydantic_settings import BaseSettings, SettingsConfigDict

# This allows values ​​to be read automatically from .env and environment variables.

Environment = Literal["local", "test", "staging", "production"]
# allowed values


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Additional values ​​in .env that are not defined in Settings are ignored.
        populate_by_name=True,  # Allows setting values ​​using both field names and aliases.
    )

    environment: Environment = Field(default="local", alias="APP_ENV")
    app_name: str = Field(default="llm-reliability-platform", alias="APP_NAME")
    api_title: str = "LLM Reliability API"
    debug: bool = Field(default=False, alias="APP_DEBUG")
    service_name: str = Field(default="llm-reliability-api", alias="OTEL_SERVICE_NAME")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")


@lru_cache  # ensures that Settings() is not rebuilt every time
def get_settings() -> Settings:
    return Settings()
