import copy

import pytest

from src import app as app_module
from httpx import AsyncClient


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activities dict between tests."""
    original = copy.deepcopy(app_module.activities)
    yield
    app_module.activities = original


@pytest.fixture
async def client():
    """Provide an `httpx.AsyncClient` against the FastAPI app."""
    async with AsyncClient(app=app_module.app, base_url="http://test") as ac:
        yield ac
