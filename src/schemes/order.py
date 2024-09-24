
from pydantic import BaseModel
from datetime import datetime


class OrderBase(BaseModel):
    pass


class OrderCreate(OrderBase):
    name: str


class Order(OrderCreate):
    id: int
    date_posted: datetime

