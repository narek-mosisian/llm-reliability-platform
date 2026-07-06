import logging
import sys
from typing import cast

import structlog

from llm_reliability.core.config import Settings


def configure_logging(settings: Settings) -> None:
    log_level = _resolve_log_level(settings.log_level)
    # Reads e.g. B. "INFO" from the settings and converts it into the internal logging value.

    logging.basicConfig(
        format="%(message)s",
        # Logs should only output the actual message.
        # No extra Python format like time, level etc.
        # because structlog does that later itself as JSON.
        level=log_level,  # sets the minimum log level
        stream=sys.stdout,
        force=True,  # Overwrites existing logging configurations.
    )

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            # adds context variables to the log (e.g.: request_id, user_id, trace_id)
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(log_level),
        # Ensures that logs below the set level are filtered.
        # e.g.: with INFO, DEBUG logs are ignored
        logger_factory=structlog.stdlib.LoggerFactory(),
        # structlog uses the normal Python logging system in the background
        # (structlog creates nice structured logs, but passes them to the
        # normal Python logging system at the end)
        cache_logger_on_first_use=True,
        # Loggers are cached the first time they are used so that they are not always recreated.
    )


def _resolve_log_level(log_level: str) -> int:
    return cast(int, getattr(logging, log_level.upper(), logging.INFO))
    # to tell mypy that it is an int
    # logging.INFO as a fallback if the log_level doesn't make sense
