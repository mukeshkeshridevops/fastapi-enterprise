import os

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Auth"])


class Login(BaseModel):
    username: str
    password: str


VALID_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
VALID_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin")


@router.post("/login")
def login(d: Login):
    return (
        {
            "access_token": "demo-token",  # nosec
            "token_type": "bearer",  # nosec
        }
        if d.username == VALID_USERNAME and d.password == VALID_PASSWORD
        else (_ for _ in ()).throw(
            HTTPException(status_code=401, detail="Invalid credentials")
        )
    )
