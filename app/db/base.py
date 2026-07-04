from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy ORM models."""

    pass


# Import ORM models here so Alembic can discover them.
# Example:
# from app.models.employee import Employee
# from app.models.user import User
