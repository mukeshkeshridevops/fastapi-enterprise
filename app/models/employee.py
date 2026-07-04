from sqlalchemy.orm import Mapped,mapped_column
from app.db.base import Base
class Employee(Base):
    __tablename__='employees'
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    department:Mapped[str]
    salary:Mapped[float]
