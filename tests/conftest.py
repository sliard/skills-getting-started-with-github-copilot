import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


_BASELINE_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Reset global in-memory state before and after each test for isolation.
    activities.clear()
    activities.update(copy.deepcopy(_BASELINE_ACTIVITIES))
    yield
    activities.clear()
    activities.update(copy.deepcopy(_BASELINE_ACTIVITIES))