from fastapi.testclient import TestClient

from llm_reliability.core.errors import ApplicationError
from llm_reliability.main import create_app


def test_application_error_returns_consistent_response() -> None:
    app = create_app()

    @app.get("/test-error")
    # creates a new test endpoint just for this test
    async def test_error() -> None:
        # When /test-error is called, this function runs.
        raise ApplicationError(
            # Intentionally raises an ApplicationError. (the test deliberately provokes an error)
            "Test error.",
            status_code=400,
            error_code="test_error",
            details={"reason": "testing"},
        )

    client = TestClient(app)

    response = client.get("/test-error")

    assert response.status_code == 400
    assert response.json() == {
        "error": "test_error",
        "message": "Test error.",
        "status_code": 400,
        "details": {
            "reason": "testing",
        },
    }
