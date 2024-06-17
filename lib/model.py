from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(cls).get(id)

    @classmethod
    def create(cls, session, name, email):
        customer = cls(name=name, email=email)
        session.add(customer)
        session.commit()
        return customer

    @classmethod
    def update(cls, session, id, name=None, email=None):
        customer = cls.get_by_id(session, id)
        if customer:
            if name:
                customer.name = name
            if email:
                customer.email = email
            session.commit()
        return customer

    @classmethod
    def delete(cls, session, id):
        customer = cls.get_by_id(session, id)
        if customer:
            session.delete(customer)
            session.commit()
            return True
        return False

class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(cls).get(id)

    @classmethod
    def create(cls, session, item_name, price):
        menu_item = cls(item_name=item_name, price=price)
        session.add(menu_item)
        session.commit()
        return menu_item

    @classmethod
    def update(cls, session, id, item_name=None, price=None):
        menu_item = cls.get_by_id(session, id)
        if menu_item:
            if item_name:
                menu_item.item_name = item_name
            if price:
                menu_item.price = price
            session.commit()
        return menu_item

    @classmethod
    def delete(cls, session, id):
        menu_item = cls.get_by_id(session, id)
        if menu_item:
            session.delete(menu_item)
            session.commit()
            return True
        return False

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer")

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(cls).get(id)

    @classmethod
    def create(cls, session, customer_id):
        order = cls(customer_id=customer_id)
        session.add(order)
        session.commit()
        return order

    @classmethod
    def update(cls, session, id, customer_id=None, order_date=None):
        order = cls.get_by_id(session, id)
        if order:
            if customer_id:
                order.customer_id = customer_id
            if order_date:
                order.order_date = order_date
            session.commit()
        return order

    @classmethod
    def delete(cls, session, id):
        order = cls.get_by_id(session, id)
        if order:
            session.delete(order)
            session.commit()
            return True
        return False

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    menu_id = Column(Integer, ForeignKey('menu.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    order = relationship("Order")
    menu_item = relationship("Menu")

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(cls).get(id)

    @classmethod
    def create(cls, session, order_id, menu_id, quantity):
        order_item = cls(order_id=order_id, menu_id=menu_id, quantity=quantity)
        session.add(order_item)
        session.commit()
        return order_item

    @classmethod
    def update(cls, session, id, order_id=None, menu_id=None, quantity=None):
        order_item = cls.get_by_id(session, id)
        if order_item:
            if order_id:
                order_item.order_id = order_id
            if menu_id:
                order_item.menu_id = menu_id
            if quantity:
                order_item.quantity = quantity
            session.commit()
        return order_item

    @classmethod
    def delete(cls, session, id):
        order_item = cls.get_by_id(session, id)
        if order_item:
            session.delete(order_item)
            session.commit()
            return True
        return False

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    menu_id = Column(Integer, ForeignKey('menu.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String)

    customer = relationship("Customer")
    menu_item = relationship("Menu")

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(cls).get(id)

    @classmethod
    def create(cls, session, customer_id, menu_id, rating, comment):
        review = cls(customer_id=customer_id, menu_id=menu_id, rating=rating, comment=comment)
        session.add(review)
        session.commit()
        return review

    @classmethod
    def update(cls, session, id, rating=None, comment=None):
        review = cls.get_by_id(session, id)
        if review:
            if rating is not None:
                review.rating = rating
            if comment:
                review.comment = comment
            session.commit()
        return review

    @classmethod
    def delete(cls, session, id):
        review = cls.get_by_id(session, id)
        if review:
            session.delete(review)
            session.commit()
            return True
        return False
# class Review(Base):
#     __tablename__ = 'reviews'
#     id = Column(Integer, primary_key=True)
#     customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
#     menu_id = Column(Integer, ForeignKey('menu.id'), nullable=False)
#     rating = Column(Integer, nullable=False)

#     customer = relationship("Customer", back_populates="reviews")
#     menu_item = relationship("Menu", back_populates="reviews")

#     @classmethod
#     def get_all(cls, session):
#         return session.query(cls).all()

#     @classmethod
#     def get_by_id(cls, session, id):
#         return session.query(cls).get(id)

#     @classmethod
#     def create(cls, session, customer_id, menu_id, rating):
#         review = cls(customer_id=customer_id, menu_id=menu_id, rating=rating)
#         session.add(review)
#         session.commit()
#         return review

#     @classmethod
#     def update(cls, session, id, rating=None):
#         review = cls.get_by_id(session, id)
#         if review:
#             if rating is not None:
#                 review.rating = rating
#             session.commit()
#         return review

#     @classmethod
#     def delete(cls, session, id):
#         review = cls.get_by_id(session, id)
#         if review:
#             session.delete(review)
#             session.commit()
#             return True
#         return False

# # Function to configure relationships
# def configure_relationships():
#     from models import Customer, Menu, Review
#     Customer.reviews = relationship("Review", back_populates="customer")
#     Menu.reviews = relationship("Review", back_populates="menu_item")

# configure_relationships()
# configure_mappers()
