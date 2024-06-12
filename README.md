# Food Ordering System 🥡🍽️

## Overview
The Food Ordering System is a relational database project designed to manage menu items, their prices, customer orders, and reviews in a restaurant or food service setting. This system helps to efficiently organize and link various pieces of information, ensuring smooth operations and enhanced customer experience.

## Database Structure
The database consists of four main tables: `Menu`, `Customer`, `Orders`, and `Reviews`. Each table is designed to store specific information and maintain relationships with other tables for comprehensive data management.

### Tables and Their Elements

#### 1. Menu Table
The `Menu` table stores information about the food items available on the menu.
- **menu_id**: Integer, Primary Key - A unique identifier for each menu item.
- **name**: Textg - The name of the menu item.
- **description**: Text - A description of the menu item.
- **category**: Text - The category of the menu item (e.g., appetizer, main course).
- **price**: Decimal - The price of the menu item.

#### 2. Customer Table
The `Customer` table stores information about customers.
- **customer_id**: Integer, Primary Key - A unique identifier for each customer.
- **name**: Text - The name of the customer.
- **email**: Text - The email of the customer.
- **phone**: Integer - The phone number of the customer.

#### 3. Orders Table
The `Orders` table stores details about customer orders, linking them to the menu items they have ordered and the customer who placed the order.
- **order_id**: Integer, Primary Key - A unique identifier for each order.
- **menu_id**: Integer, Foreign Key - Links to the `menu_id` in the Menu table.
- **customer_id**: Integer, Foreign Key - Links to the `customer_id` in the Customer table.
- **quantity**: Integer - The quantity of the menu item ordered.
- **order_date**: DateTime - The date and time when the order was placed.

#### 4. Reviews Table
The `Reviews` table stores reviews given by customers for each menu item.
- **review_id**: Integer, Primary Key - A unique identifier for each review.
- **order_id**: Integer, Foreign Key - Links to the `order_id` in the Orders table.
- **rating**: Integer - The rating given by the customer (e.g., 1 to 5 stars).
- **comment**: Text - The review comment.
- **review_date**: DateTime - The date and time of the review.

## Relationships Between Tables
1. **Orders and Menu:**
   - The `Orders` table includes a `menu_id` foreign key, linking each order to a specific menu item in the `Menu` table. This tracks which menu items were ordered.
2. **Orders and Customer:**
   - The `Orders` table includes a `customer_id` foreign key, linking each order to a specific customer in the `Customer` table. This tracks who placed the order.
3. **Orders and Reviews:**
   - The `Reviews` table includes an `order_id` foreign key, linking each review to a specific order in the `Orders` table. This allows each order to have an associated review, including a rating and a comment.

## ERD Relationship Diagram

```plaintext
Menu (1) ---------< (N) Orders >--------- (1) Customer
  |                     |                     |
menu_id (PK)           menu_id (FK)          customer_id (PK)
  |                    customer_id (FK)        |
  |                      |                    name
  |                     /                      email
Reviews >--------------/                       phone
  |
review_id (PK)
order_id (FK)
-- Menu Table  

CREATE TABLE Menu (
    menu_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50),
    price DECIMAL(10, 2)
);

-- Customer Table
CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(15)
);

-- Orders Table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    menu_id INT,
    customer_id INT,
    quantity INT,
    order_date DATETIME,
    FOREIGN KEY (menu_id) REFERENCES Menu(menu_id),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

-- Reviews Table
CREATE TABLE Reviews (
    review_id INT PRIMARY KEY,
    order_id INT,
    rating INT,
    comment TEXT,
    review_date DATETIME,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);
