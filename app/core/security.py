from datetime import datetime, timedelta

from jose import jwt

from app.core.config import settings


def create_access_token(subject: str, minutes: int = 30):
    payload = {
        "sub": subject,
        "exp": datetime.utcnow() + timedelta(minutes=minutes),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def verify_token(token: str):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
