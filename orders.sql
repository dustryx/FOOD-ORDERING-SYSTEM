-- orders.sql
CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    order_date DATETIME,
    FOREIGN KEY (customer_id) REFERENCES Customers(id)
);

CREATE TABLE OrderItems (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    menu_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (menu_id) REFERENCES Menu(menu_id)
);

INSERT INTO Orders (customer_id, order_date) VALUES (3, '2023-06-13 14:00:00');

SELECT * FROM Orders;

UPDATE Orders SET order_date = '2023-06-14 15:00:00' WHERE order_id = 1;

DELETE FROM Orders WHERE order_id = 2;

INSERT INTO OrderItems (order_id, menu_id, quantity) VALUES (1, 3, 2);

SELECT * FROM OrderItems WHERE order_id = 1;

UPDATE OrderItems SET quantity = 3 WHERE order_item_id = 1;

DELETE FROM OrderItems WHERE order_item_id = 2;