from pydantic import BaseModel


class Base(BaseModel):
    pass
    # id: int


class OrderItems(Base):
    id: int
    orders_id: int
    products_id: int


class Orders(OrderItems):
    id: int
    users_id: int
    statuses_id: int


class Statuses(Orders):
    # id: int
    name: str


class Users(Orders):
    # id: int
    name: str
    email: str


class Products(OrderItems):
    # id: int
    title: str
    description: str
    category_id: int


class Categories(Products):
    # id: int
    name: str

    # class Config:
    #     orm_mode = True
