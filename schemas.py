from pydantic import BaseModel
from typing import List

class OrderBase(BaseModel):
    item: str

class OrderRead(OrderBase):
    id: int

    class Config:
        orm_mode = True

class CustomerBase(BaseModel):
    name: str

class CustomerRead(CustomerBase):
    id: int
    orders: List[OrderRead] = []

    class Config:
        orm_mode = True
