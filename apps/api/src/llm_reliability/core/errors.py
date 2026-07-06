"""Meaning of this file:

If an error happens in the API, you shouldn't get some unclear Python error message,
but rather a consistent JSON response.
"""

from typing import Any

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    error: str
    message: str
    status_code: int
    details: dict[str, Any] | None = None


class ApplicationError(Exception):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    error_code = "application_error"
    message = "An application error occurred."

    def __init__(
        self,
        message: str | None = None,
        *,
        # Everything after that must be passed as a named argument.
        # e.g: ApplicationError(status_code=400)
        status_code: int | None = None,
        error_code: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        self.message = message if message is not None else self.message
        self.status_code = status_code if status_code is not None else self.status_code
        self.error_code = error_code if error_code is not None else self.error_code
        self.details = details

        super().__init__(self.message)
        # Invokes the constructor of the parent class Exception.
        # This is important so that the error is a “real” Python error.


class ResourceNotFoundError(ApplicationError):
    status_code = status.HTTP_404_NOT_FOUND
    error_code = "not_found"
    message = "The requested resource was not found."


async def application_error_handler(_request: Request, exc: Exception) -> JSONResponse:
    # _request: Request is the HTTP request where the error occurred
    # exc: Exception is the actual error that happened
    # The underscore means that the function must accept this parameter,
    # but deliberately does not use it internally.
    if not isinstance(exc, ApplicationError):
        return await unhandled_error_handler(_request, exc)
        # If exc is not an ApplicationError, the error is propagated to the general error handler.

    return _error_response(
        error=exc.error_code,
        message=exc.message,
        status_code=exc.status_code,
        details=exc.details,
    )


async def unhandled_error_handler(_request: Request, _exc: Exception) -> JSONResponse:
    return _error_response(
        error="internal_server_error",
        message="An unexpected error occurred.",
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        ApplicationError, application_error_handler
    )  # also applies to subclasses
    app.add_exception_handler(Exception, unhandled_error_handler)


# The underscore means that this function is only intended internally
# for this file/module.
def _error_response(
    *,
    error: str,
    message: str,
    status_code: int,
    details: dict[str, Any] | None = None,
) -> JSONResponse:
    response = ErrorResponse(
        error=error,
        message=message,
        status_code=status_code,
        details=details,
    )

    return JSONResponse(  # a real HTTP response is built
        status_code=status_code,
        content=response.model_dump(exclude_none=True),
        # the Pydantic model is converted into a normal Python dictionary
        # Fields with None are omitted
    )
