
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories import base
from src.schemes.order import *


class OrderRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, scheme: OrderCreate) -> OrderCreate:
        order = base.Order(
            name=scheme.name
        )

        async with self._session.begin() as session:
            session.add(order)
            await session.commit()
            return scheme

    async def get(self, scheme: Order) -> Order:
        async with self._session.begin() as session:
            if session.query(base.Order).filter(base.Order.id == scheme.id).first():
                return scheme

