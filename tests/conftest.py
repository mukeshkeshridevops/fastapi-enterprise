from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.api.v1 import auth,users,employees,departments,health
import pytest
app=FastAPI()
for r in [auth.router,users.router,employees.router,departments.router,health.router]:
    app.include_router(r,prefix="/api/v1")
@pytest.fixture
def client():
    return TestClient(app)
