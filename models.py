from sqlalchemy import Column, INT, VARCHAR, ForeignKey
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class OrderItems(Base):
    __tablename__ = 'orderItems'
    id = Column(INT, primary_key=True)
    order_id = Column(ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
    product_id = Column(ForeignKey('products.id', ondelete='CASCADE'), nullable=False)


class Orders(OrderItems):
    __tablename__ = 'orders'
    id = Column(INT, primary_key=True)
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    status_id = Column(ForeignKey('statuses.id', ondelete='CASCADE'), nullable=False)


class Statuses(Orders):
    __tablename__ = 'statuses'
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(10), unique=True, nullable=False)


class Users(Orders):
    __tablename__ = 'users'
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(24), nullable=False)
    email = Column(VARCHAR(24), unique=True, nullable=False)


class Products(OrderItems):
    __tablename__ = 'products'
    id = Column(INT, primary_key=True)
    title = Column(VARCHAR(36), nullable=False)
    description = Column(VARCHAR(140), nullable=False)
    category_id = Column(ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)


class Categories(Products):
    __tablename__ = 'categories'
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(24), unique=True, nullable=False)
