import pytest
from fastapi.testclient import TestClient

from src.app import app


@pytest.fixture
def client():
    """Provides a TestClient instance for making API requests."""
    with TestClient(app) as c:
        yield c
