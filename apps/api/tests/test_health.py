from fastapi.testclient import TestClient

# so that you can call the API in the test without starting the real server
from llm_reliability.core.config import Settings
from llm_reliability.main import create_app


# pytest recognizes the function as a test because it starts with test_
def test_health_endpoint_returns_ok() -> None:
    client = TestClient(create_app())
    # creates a test version of the API with default settings

    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "llm-reliability-api",
        "version": "0.1.0",
    }


def test_health_endpoint_uses_configured_service_name() -> None:
    client = TestClient(
        create_app(
            Settings(
                # overwrite the standard configuration in the test
                environment="test",  # instead of “local”
                service_name="custom-api",  # instead of llm-reliability-api"
            )
        )
    )

    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json()["service"] == "custom-api"


def test_openapi_schema_is_available() -> None:
    client = TestClient(create_app())

    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert response.json()["info"]["title"] == "LLM Reliability API"
