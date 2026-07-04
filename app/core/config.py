from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME = "Enterprise FastAPI"
    API_V1 = "/api/v1"
    SECRET_KEY = "change-me"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    DATABASE_URL = "postgresql://user:password@localhost:5432/appdb"


settings = Settings()
