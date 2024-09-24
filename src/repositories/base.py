
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, BigInteger, DateTime

from datetime import datetime


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    date_posted: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now())

    def __repr__(self):
        return f"Order(id: {self.id!r}, name: {self.name!r}, date_posted: {self.date_posted!r}"
