import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.api.v1 import auth, departments, employees, health, users

app = FastAPI()
for r in [
    auth.router,
    users.router,
    employees.router,
    departments.router,
    health.router,
]:
    app.include_router(r, prefix="/api/v1")


@pytest.fixture
def client():
    return TestClient(app)
