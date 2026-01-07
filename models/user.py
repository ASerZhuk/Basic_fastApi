from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    first_name: Mapped[str | None] = mapped_column(String(length=100), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(length=100), nullable=True)

