# FOOD-ORDERING-SYSTEM

## Overview
The Food Ordering  System is a relational database project designed to manage menu items, their prices, customer orders, and reviews in a restaurant or food service setting. This system helps to efficiently organize and link various pieces of information, ensuring smooth operations and enhanced customer experience.

## Database Structure
The database consists of four main tables: `Menu`, `Prices`, `Orders`, and `Reviews`. Each table is designed to store specific information and maintain relationships with other tables for comprehensive data management.

### Tables and Their Elements

#### 1. Menu Table
The `Menu` table stores information about the food items available on the menu.

- **menu_id**: Integer, Primary Key - A unique identifier for each menu item.
- **name**: String - The name of the menu item.
- **description**: String - A description of the menu item.
- **category**: String - The category of the menu item (e.g., appetizer, main course).

#### 2. Prices Table
The `Prices` table stores pricing details for each menu item, allowing for different sizes or variations.

- **price_id**: Integer, Primary Key - A unique identifier for each price entry.
- **menu_id**: Integer, Foreign Key - Links to the `menu_id` in the Menu table.
- **price**: Decimal - The price of the menu item.
- **size**: String - The size or variation of the menu item (e.g., small, medium, large).

#### 3. Orders Table
The `Orders` table stores details about customer orders, linking them to the menu items they have ordered.

- **order_id**: Integer, Primary Key - A unique identifier for each order.
- **menu_id**: Integer, Foreign Key - Links to the `menu_id` in the Menu table.
- **menu**: Integer - The quantity of the menu item ordered.
- **order_date**: DateTime - The date and time when the order was placed.

#### 4. Reviews Table
The `Reviews` table stores reviews given by customers for each menu item.

- **review_id**: Integer, Primary Key - A unique identifier for each review.
- **order_id**: Integer, Foreign Key - Links to the `order_id` in the Orders table.
- **rating**: Integer - The rating given by the customer (e.g., 1 to 5 stars).
- **comment**: String - The review comment.
- **review_date**: DateTime - The date and time of the review.

## Relationships Between Tables

1. **Menu and Prices:**
   - The `Prices` table includes a `menu_id` foreign key, linking each price entry to a specific menu item in the `Menu` table. This allows each menu item to have multiple price entries for different sizes or variations.

2. **Orders and Menu:**
   - The `Orders` table includes a `menu_id` foreign key, linking each order to a specific menu item in the `Menu` table. This tracks which menu items were ordered.

3. **Orders and Reviews:**
   - The `Reviews` table includes an `order_id` foreign key, linking each review to a specific order in the `Orders` table. This allows each order to have an associated review, including a rating and a comment.

## SQL Implementation

### Create Tables

```sql
-- Menu Table
CREATE TABLE Menu (
    menu_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50)
);

-- Prices Table
CREATE TABLE Prices (
    price_id INT PRIMARY KEY,
    menu_id INT,
    price DECIMAL(10, 2),
    size VARCHAR(50),
    FOREIGN KEY (menu_id) REFERENCES Menu(menu_id)
);

-- Orders Table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    menu_id INT,
    quantity INT,
    order_date DATETIME,
    FOREIGN KEY (menu_id) REFERENCES Menu(menu_id)
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
