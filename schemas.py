from datetime import date
from pydantic import BaseModel


class Base(BaseModel):
    pass


class OrderItems(Base):
    id: int
    order_id: int
    product_id: int


class Orders(OrderItems):
    id: int
    user_id: int
    status_id: int


class Statuses(Orders):
    id: int
    name: str


class Users(Orders):
    id: int
    name: str
    email: str


class Products(OrderItems):
    id: int
    title: str
    description: str
    category_id: int


class Categories(Products):
    id: int
    name: str

    class Config:
        orm_mode = True
