
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from src.config import SQL_ALCHEMY_DATABASE_URL

from src.repositories.order import OrderRepository

# --- Database init
engine = create_async_engine(SQL_ALCHEMY_DATABASE_URL)
session = AsyncSession(bind=engine, autocommit=False)


# --- Repositories
order_repository = OrderRepository(session)


def get_order_repository() -> OrderRepository:
    return order_repository
