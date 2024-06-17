from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Customer, Menu, Order, OrderItem, Review
from datetime import datetime

# Connect to the specified database
engine = create_engine('sqlite:///FOOD-ORDERING-SYSTEM/food_ordering.db')
Base.metadata.create_all(engine)  # Ensure the tables are created

Session = sessionmaker(bind=engine)
session = Session()

def exit_program():
    print("Always welcomed again.....😍.")
    session.close()
    exit()

# Customer Helpers
def list_customers():
    customers = Customer.get_all(session)
    for customer in customers:
        print(f"ID: {customer.id}, Name: {customer.name}, Email: {customer.email}")

def find_customer_by_id():
    customer_id = int(input("Enter Customer ID: "))
    customer = Customer.get_by_id(session, customer_id)
    if customer:
        print(f"ID: {customer.id}, Name: {customer.name}, Email: {customer.email}")
    else:
        print(f"Customer with ID: {customer_id} not found.")

def create_customer():
    name = input("Enter Customer Name: ")
    email = input("Enter Customer Email: ")
    customer = Customer.create(session, name=name, email=email)
    print(f"Created customer with ID: {customer.id}")

def update_customer():
    customer_id = int(input("Enter Customer ID: "))
    name = input("Enter new name (leave blank to keep current): ")
    email = input("Enter new email (leave blank to keep current): ")
    customer = Customer.update(session, customer_id, name=name or None, email=email or None)
    if customer:
        print(f"Updated customer with ID: {customer.id}")
    else:
        print(f"Customer with ID: {customer_id} not found.")

def delete_customer():
    customer_id = int(input("Enter Customer ID: "))
    success = Customer.delete(session, customer_id)
    if success:
        print(f"Deleted customer with ID: {customer_id}")
    else:
        print(f"Customer with ID: {customer_id} not found.")

# Menu Helpers
def list_menu():
    menu_items = Menu.get_all(session)
    for item in menu_items:
        print(f"ID: {item.id}, Item: {item.item_name}, Price: {item.price}")

def find_menu_by_id():
    menu_id = int(input("Enter Menu ID: "))
    item = Menu.get_by_id(session, menu_id)
    if item:
        print(f"ID: {item.id}, Item: {item.item_name}, Price: {item.price}")
    else:
        print(f"Menu item with ID: {menu_id} not found.")

def create_menu_item():
    item_name = input("Enter Item Name: ")
    price = float(input("Enter Price: "))
    item = Menu.create(session, item_name=item_name, price=price)
    print(f"Created menu item with ID: {item.id}")

def update_menu_item():
    menu_id = int(input("Enter Menu ID: "))
    item_name = input("Enter new item name (leave blank to keep current): ")
    price = input("Enter new price (leave blank to keep current): ")
    item = Menu.update(session, menu_id, item_name=item_name or None, price=float(price) if price else None)
    if item:
        print(f"Updated menu item with ID: {item.id}")
    else:
        print(f"Menu item with ID: {menu_id} not found.")

def delete_menu_item():
    menu_id = int(input("Enter Menu ID: "))
    success = Menu.delete(session, menu_id)
    if success:
        print(f"Deleted menu item with ID: {menu_id}")
    else:
        print(f"Menu item with ID: {menu_id} not found.")

# Order Helpers
def list_orders():
    orders = Order.get_all(session)
    for order in orders:
        print(f"ID: {order.id}, Customer ID: {order.customer_id}, Order Date: {order.order_date}")

def find_order_by_id():
    order_id = int(input("Enter Order ID: "))
    order = Order.get_by_id(session, order_id)
    if order:
        print(f"ID: {order.id}, Customer ID: {order.customer_id}, Order Date: {order.order_date}")
    else:
        print(f"Order with ID: {order_id} not found.")

def create_order():
    customer_id = int(input("Enter Customer ID: "))
    order = Order.create(session, customer_id=customer_id)
    print(f"Created order with ID: {order.id}")

def update_order():
    order_id = int(input("Enter Order ID: "))
    customer_id = input("Enter new customer ID (leave blank to keep current): ")
    order_date = input("Enter new order date (YYYY-MM-DD HH:MM:SS) (leave blank to keep current): ")
    order = Order.update(session, order_id, customer_id=int(customer_id) if customer_id else None, order_date=datetime.strptime(order_date, '%Y-%m-%d %H:%M:%S') if order_date else None)
    if order:
        print(f"Updated order with ID: {order.id}")
    else:
        print(f"Order with ID: {order.id} not found.")

def delete_order():
    order_id = int(input("Enter Order ID: "))
    success = Order.delete(session, order_id)
    if success:
        print(f"Deleted order with ID: {order_id}")
    else:
        print(f"Order with ID: {order_id} not found.")

# OrderItem Helpers
def list_order_items():
    order_items = OrderItem.get_all(session)
    for item in order_items:
        print(f"ID: {item.id}, Order ID: {item.order_id}, Menu ID: {item.menu_id}, Quantity: {item.quantity}")

def find_order_item_by_id():
    order_item_id = int(input("Enter Order Item ID: "))
    item = OrderItem.get_by_id(session, order_item_id)
    if item:
        print(f"ID: {item.id}, Order ID: {item.order_id}, Menu ID: {item.menu_id}, Quantity: {item.quantity}")
    else:
        print(f"Order item with ID: {order_item_id} not found.")

def create_order_item():
    order_id = int(input("Enter Order ID: "))
    menu_id = int(input("Enter Menu ID: "))
    quantity = int(input("Enter Quantity: "))
    item = OrderItem.create(session, order_id=order_id, menu_id=menu_id, quantity=quantity)
    print(f"Created order item with ID: {item.id}")

def update_order_item():
    order_item_id = int(input("Enter Order Item ID: "))
    order_id = input("Enter new order ID (leave blank to keep current): ")
    menu_id = input("Enter new menu ID (leave blank to keep current): ")
    quantity = input("Enter new quantity (leave blank to keep current): ")
    item = OrderItem.update(session, order_item_id, order_id=int(order_id) if order_id else None, menu_id=int(menu_id) if menu_id else None, quantity=int(quantity) if quantity else None)
    if item:
        print(f"Updated order item with ID: {item.id}")
    else:
        print(f"Order item with ID: {order_item_id} not found.")

def delete_order_item():
    order_item_id = int(input("Enter Order Item ID: "))
    success = OrderItem.delete(session, order_item_id)
    if success:
        print(f"Deleted order item with ID: {order_item_id}")
    else:
        print(f"Order item with ID: {order_item_id} not found.")

# Review Helpers
# def list_reviews():
#     reviews = Review.get_all(session)
#     for review in reviews:
#         print(f"ID: {review.id}, Customer ID: {review.customer_id}, Menu ID: {review.menu_id}, Rating: {review.rating}, Comment: {review.comment}")
def list_reviews():
    reviews = Review.get_all(session)
    for review in reviews:
        print(f"Review ID: {review.id}, Customer ID: {review.customer_id}, Menu ID: {review.menu_id}, Rating: {review.rating}")



def find_review_by_id():
    review_id = int(input("Enter Review ID: "))
    review = Review.get_by_id(session, review_id)
    if review:
        print(f"ID: {review.id}, Customer ID: {review.customer_id}, Menu ID: {review.menu_id}, Rating: {review.rating}, Comment: {review.comment}")
    else:
        print(f"Review with ID: {review_id} not found.")

def create_review():
    customer_id = int(input("Enter Customer ID: "))
    menu_id = int(input("Enter Menu ID: "))
    rating = int(input("Enter Rating (1-5): "))
    comment = input("Enter Comment: ")
    review = Review.create(session, customer_id=customer_id, menu_id=menu_id, rating=rating, comment=comment)
    print(f"Created review with ID: {review.id}")

def update_review():
    review_id = int(input("Enter Review ID: "))
    rating = input("Enter new rating (leave blank to keep current): ")
    comment = input("Enter new comment (leave blank to keep current): ")
    review = Review.update(session, review_id, rating=int(rating) if rating else None, comment=comment or None)
    if review:
        print(f"Updated review with ID: {review.id}")
    else:
        print(f"Review with ID: {review.id} not found.")

def delete_review():
    review_id = int(input("Enter Review ID: "))
    success = Review.delete(session, review_id)
    if success:
        print(f"Deleted review with ID: {review_id}")
    else:
        print(f"Review with ID: {review_id} not found.")
        
def main():
    while True:
        print("\nFood Ordering System")
        print("1. Customer Operations")
        print("2. Menu Operations")
        # print("3. Order Operations")
        # print("3. Review Operations")
        print("3. Order Item Operations")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            print("\nCustomer Operations:")
            print("1. List Customers")
            print("2. Find Customer by ID")
            print("3. Create Customer")
            print("4. Update Customer")
            print("5. Delete Customer")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '1':
                list_customers()
            elif sub_choice == '2':
                find_customer_by_id()
            elif sub_choice == '3':
                create_customer()
            elif sub_choice == '4':
                update_customer()
            elif sub_choice == '5':
                delete_customer()
            else:
                print("Invalid choice!")

        elif choice == '2':
            print("\nMenu Operations:")
            print("1. List Menu Items")
            print("2. Find Menu Item by ID")
            print("3. Create Menu Item")
            print("4. Update Menu Item")
            print("5. Delete Menu Item")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '1':
                list_menu()
            elif sub_choice == '2':
                find_menu_by_id()
            elif sub_choice == '3':
                create_menu_item()
            elif sub_choice == '4':
                update_menu_item()
            elif sub_choice == '5':
                delete_menu_item()
            else:
                print("Invalid choice!")

        # elif choice == '3':
        #     print("\nOrder Operations:")
        #     print("1. List Orders")
        #     print("2. Find Order by ID")
        #     print("3. Create Order")
        #     print("4. Update Order")
        #     print("5. Delete Order")
        #     sub_choice = input("Enter your choice: ")
        #     if sub_choice == '1':
        #         list_orders()
        #     elif sub_choice == '2':
        #         find_order_by_id()
        #     elif sub_choice == '3':
        #         create_order()
        #     elif sub_choice == '4':
        #         update_order()
        #     elif sub_choice == '5':
        #         delete_order()
        #     else:
        #         print("Invalid choice!")

        # elif choice == '3':
        #     print("\nReview Operations:")
        #     print("1. List Reviews")
        #     print("2. Find Review by ID")
        #     print("3. Create Review")
        #     print("4. Update Review")
        #     print("5. Delete Review")
        #     sub_choice = input("Enter your choice: ")
        #     if sub_choice == '1':
        #         list_reviews()
        #     elif sub_choice == '2':
        #         find_review_by_id()
        #     elif sub_choice == '3':
        #         create_review()
        #     elif sub_choice == '4':
        #         update_review()
        #     elif sub_choice == '5':
        #         delete_review()
        #     else:
        #         print("Invalid choice!")

        elif choice == '3':
            print("\nOrder Item Operations:")
            print("1. List Order Items")
            print("2. Find Order Item by ID")
            print("3. Create Order Item")
            print("4. Update Order Item")
            print("5. Delete Order Item")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '1':
                list_order_items()
            elif sub_choice == '2':
                find_order_item_by_id()
            elif sub_choice == '3':
                create_order_item()
            elif sub_choice == '4':
                update_order_item()
            elif sub_choice == '5':
                delete_order_item()
            else:
                print("Invalid choice!")

        elif choice == '4':
            exit_program()
        else:
            print("Invalid choice!")


# Execute the main function when the script is run
if __name__ == "__main__":
    print("\t\tWelcome customer😊")
    main()
