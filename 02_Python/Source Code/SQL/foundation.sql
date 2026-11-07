SHOW DATABASES;

USE learn_sql;

CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    full_name VARCHAR(60) NOT NULL,
    city VARCHAR(40) NULL,
    joined_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS products (
    sku CHAR(6) PRIMARY KEY,
    product_name VARCHAR(80) NOT NULL,
    price DECIMAL(8, 2) NOT NULL CHECK (price >= 0),
    stock INT NOT NULL DEFAULT 0 CHECK (stock >= 0)
);

CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    placed_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Pending', 'Paid', 'Shipped', 'Cancelled') NOT NULL DEFAULT 'Pending',
    CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id) 
);

CREATE TABLE IF NOT EXISTS order_items(
    order_id INT NOT NULL,
    sku CHAR(6) NOT NULL,
   qty INT NOT NULL CHECK (qty > 0),
   unit_price DECIMAL(8, 2) NOT NULL,
   PRIMARY KEY (order_id, sku),
   CONSTRAINT fk_items_order FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
   CONSTRAINT fk_item_product FOREIGN KEY (sku) REFERENCES products (sku)
);

SHOW TABLES;

-- DATA INSERT

-- INSERT INTO customers (email, full_name, city) VALUES
-- ('krish@example.com', 'Nandanvar Krish', 'Surat'),
-- ('dhiren@example.com', 'Singh Dhirendra', 'Vadodara'),
-- ('satyam@example.com', 'Singh Satyam', 'Mumbai'),
-- ('shubh@example.com', 'Umar Shubh', 'Surat');

-- INSERT INTO products (sku, product_name, price, stock) VALUES
-- ('P001', 'A4 Notebook', 100.0, 569),
-- ('P002', 'Gel Pen', 10.69, 150),
-- ('P003', 'Desk Lamp', 899.0, 0);

-- INSERT INTO orders (customer_id, status) VALUES
-- (1, 'Paid'),
-- (2, 'Pending'),
-- (3, 'Shipped');

SELECT * FROM customers;
SELECT * FROM products;
SELECT * FROM orders;

-- INSERT INTO products (sku, product_name, price) VALUES ('P005', 'Stapler', 120.00);

-- SELECT sku, stock FROM products WHERE sku = 'P005'


CREATE TABLE IF NOT EXISTS order_archive as SELECT * from orders WHERE 1 = 0;

DESCRIBE order_archive;
SELECT * FROM order_archive;

-- INSERT INTO order_archive SELECT * FROM orders WHERE status = 'shipped';

SELECT order_id, status FROM order_archive ORDER BY order_id;

UPDATE products SET stock = stock - 2 WHERE sku = 'P001';

SELECT sku, stock FROM products ORDER BY sku;

UPDATE orders SET status = 'paid' WHERE order_id = 2;

-- UPDATE orders SET status = 'refunded' WHERE order_id = 2;

CREATE TABLE stock_copy AS SELECT * FROM products;

UPDATE stock_copy SET stock = 0;

SELECT sku, stock FROM stock_copy ORDER BY sku;

DROP TABLE IF EXISTS stock_copy;

SELECT (SELECT COUNT(*) FROM orders WHERE order_id = 3) AS order_count, (SELECT COUNT(*) FROM order_items WHERE order_id = 3) AS line_count;

DELETE FROM orders WHERE order_id = 3;
SELECT (SELECT COUNT(*) FROM orders WHERE order_id = 3) AS order_count, (SELECT COUNT(*) FROM order_items WHERE order_id = 3) AS line_count;
CREATE TABLE lines_copy AS SELECT * FROM order_items;

TRUNCATE TABLE lines_copy;

SELECT COUNT(*) FROM lines_copy;

DROP TABLE lines_copy;

SELECT * FROM lines_copy;

INSERT INTO products (sku, product_name, price, stock) VALUES ('P001', 'A4 Notebook', 100.0, 5)
ON DUPLICATE KEY UPDATE stock = stock + VALUES(stock);

SELECT sku, stock FROM products WHERE sku = 'P001';
SELECT sku, stock FROM products WHERE sku = 'P002';

START TRANSACTION;
UPDATE products SET stock = stock - 5 WHERE sku = 'P002';
ROLLBACK;

SELECT sku, stock FROM products WHERE sku = 'P002';

START TRANSACTION;
INSERT INTO orders (customer_id, status) VALUES (1, 'pending');
UPDATE products SET stock = stock - 5 WHERE sku = 'P002';
COMMIT;

SELECT sku, stock FROM products WHERE sku = 'P002';

START TRANSACTION;
UPDATE products SET stock = stock - 1000 WHERE sku = 'P003';
COMMIT;

SELECT sku, stock FROM products WHERE sku = 'P003';

ALTER TABLE customers ADD COLUMN phone VARCHAR(15) NULL AFTER city;

ALTER TABLE customers MODIFY COLUMN full_name VARCHAR(100) NOT NULL;

ALTER TABLE customers CHANGE COLUMN city town VARCHAR(40) NULL;

DESCRIBE customers;

ALTER TABLE products ADD CONSTRAINT chk_name_len CHECK (CHAR_LENGTH(product_name) >= 2);

INSERT INTO products (sku, product_name, price) VALUES ('P009', 'X', 1.00);

ALTER TABLE customers DROP COLUMN phone;

CREATE INDEX idx_orders_status ON orders (status);

SELECT INDEX_NAME, COLUMN_NAME FROM information_schema.STATISTICS WHERE TABLE_SCHEMA = 'learn_sql' AND TABLE_NAME = 'orders' ORDER BY INDEX_NAME;

DROP INDEX idx_orders_status ON orders;

RENAME TABLE order_archive TO archived_orders;

SHOW TABLES LIKE 'archived%';

DROP TABLE archived_orders;

SELECT * FROM archived_orders;


