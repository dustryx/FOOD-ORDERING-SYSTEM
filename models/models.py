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

    @classmethod
    def create(cls, name, email):
        new_customer = cls(name=name, email=email)
        session.add(new_customer)
        session.commit()
        return new_customer

    @classmethod
    def get_by_id(cls, customer_id):
        return session.query(cls).filter_by(id=customer_id).first()

    # Other ORM methods for Customer class

class Menu(Base):
    __tablename__ = 'menu'

    menu_id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    # ORM methods for Menu class

class Review(Base):
    __tablename__ = 'reviews'

    review_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    menu_id = Column(Integer, ForeignKey('menu.menu_id'))
    rating = Column(Integer, nullable=False)
    comment = Column(String)
    review_date = Column(DateTime, default=datetime.now)

    customer = relationship('Customer', back_populates='reviews')
    menu = relationship('Menu')

    # ORM methods for Review class

class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    order_date = Column(DateTime, default=datetime.now)

    customer = relationship('Customer', back_populates='orders')
    order_items = relationship('OrderItem', back_populates='order')

    @classmethod
    def create(cls, customer_id, order_date):
        new_order = cls(customer_id=customer_id, order_date=order_date)
        session.add(new_order)
        session.commit()
        return new_order

    @classmethod
    def get_by_id(cls, order_id):
        return session.query(cls).filter_by(order_id=order_id).first()

    # Other ORM methods for Order class

class OrderItem(Base):
    __tablename__ = 'order_items'

    order_item_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    menu_id = Column(Integer, ForeignKey('menu.menu_id'))
    quantity = Column(Integer, nullable=False)

    order = relationship('Order', back_populates='order_items')
    menu = relationship('Menu')

    # ORM methods for OrderItem class

# Create the database engine and tables
engine = create_engine('sqlite:///food_ordering.db')
Base.metadata.create_all(engine)
