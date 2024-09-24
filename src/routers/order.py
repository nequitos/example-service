
from src.depends import get_order_repository
from src.repositories.order import OrderRepository
from src.schemes.order import *

from fastapi import APIRouter, Depends


router = APIRouter(prefix="/order", tags=["order"])


@router.post(
    "",
    response_model=OrderCreate,
    description="Create order"
)
async def create(
    order: OrderCreate,
    order_repository: OrderRepository = Depends(get_order_repository)
) -> OrderCreate:
    response = await order_repository.create(order)
    return response


@router.get(
    "",
    response_model=Order,
    description="Get order"
)
async def get(
    order: Order,
    order_repository: OrderRepository = Depends(get_order_repository)
) -> Order:

    response = await order_repository.get(order)
    return response