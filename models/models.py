from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    orders = relationship('Order', back_populates='customer')
    reviews = relationship('Review', back_populates='customer')

    @classmethod
    def create(cls, name, email):
        new_customer = cls(name=name, email=email)
        session.add(new_customer)
        session.commit()
        return new_customer

    @classmethod
    def get_by_id(cls, customer_id):
        return session.query(cls).filter_by(id=customer_id).first()


class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    item_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    menu_id = Column(Integer, ForeignKey('menu.id'))
    rating = Column(Integer, nullable=False)

    customer = relationship('Customer', back_populates='reviews')
    menu = relationship('Menu')


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))

    customer = relationship('Customer', back_populates='orders')
    order_items = relationship('OrderItem', back_populates='order')

    @classmethod
    def create(cls, customer_id):
        new_order = cls(customer_id=customer_id)
        session.add(new_order)
        session.commit()
        return new_order

    @classmethod
    def get_by_id(cls, order_id):
        return session.query(cls).filter_by(id=order_id).first()


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    menu_id = Column(Integer, ForeignKey('menu.id'))
    quantity = Column(Integer, nullable=False)

    order = relationship('Order', back_populates='order_items')
    menu = relationship('Menu')

# Create the database engine and tables
engine = create_engine('sqlite:///food_ordering.db')
Base.metadata.create_all(engine)
