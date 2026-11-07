SHOW DATABASES;

CREATE DATABASE IF NOT EXISTS shop_ref CHARACTER SET utf8mb4;

USE shop_ref;

CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    email       VARCHAR(100) NOT NULL UNIQUE,
    full_name   VARCHAR(60)  NOT NULL,
    city        VARCHAR(40)  NULL,
    joined_at   DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS products (
    sku          CHAR(6)       PRIMARY KEY,
    product_name VARCHAR(80)   NOT NULL,
    price        DECIMAL(8,2)  NOT NULL CHECK (price >= 0),
    stock        INT           NOT NULL DEFAULT 0 CHECK (stock >= 0)
);
CREATE TABLE IF NOT EXISTS orders (
    order_id    INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    placed_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status      ENUM('pending','paid','shipped','cancelled') NOT NULL DEFAULT 'pending',
    CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
CREATE TABLE IF NOT EXISTS order_items (
    order_id   INT NOT NULL,
    sku        CHAR(6) NOT NULL,
    qty        INT NOT NULL CHECK (qty > 0),
    unit_price DECIMAL(8,2) NOT NULL,
    PRIMARY KEY (order_id, sku),
    CONSTRAINT fk_items_order   FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    CONSTRAINT fk_items_product FOREIGN KEY (sku) REFERENCES products(sku)
);

-- INSERT INTO customers (email, full_name, city) VALUES
--   ('asha@example.com', 'Asha Rao', 'Pune'), ('ben@example.com', 'Ben Carter', 'Mumbai'), ('chen@example.com', 'Chen Wei', 'Pune');
-- INSERT INTO products (sku, product_name, price, stock) VALUES
--   ('P001', 'Notebook A5', 49.50, 20), ('P002', 'Gel pen', 12.00, 150), ('P003', 'Desk lamp', 899.00, 0);
-- INSERT INTO orders (customer_id, status) VALUES (1, 'paid'), (2, 'pending'), (3, 'shipped');
-- INSERT INTO order_items (order_id, sku, qty, unit_price) VALUES
--   (1, 'P001', 2, 49.50), (1, 'P002', 5, 12.00), (2, 'P003', 1, 899.00), (3, 'P002', 10, 12.00);

-- INSERT INTO products (sku, product_name, price, stock) VALUES ('P006', 'Sticky notes', 35.00, 40)
-- ON DUPLICATE KEY UPDATE stock = stock + VALUES(stock);
-- INSERT INTO products (sku, product_name, price, stock) VALUES ('P002', 'Gel pen', 12.00, 30)
-- ON DUPLICATE KEY UPDATE stock = stock + VALUES(stock);

-- START TRANSACTION;
-- INSERT INTO orders (customer_id, status) VALUES (2, 'paid');
-- INSERT INTO order_items (order_id, sku, qty, unit_price) VALUES (LAST_INSERT_ID(), 'P006', 3, 35.00);
-- UPDATE products SET stock = stock - 3 WHERE sku = 'P006';
-- COMMIT;

-- START TRANSACTION;
-- INSERT INTO orders (customer_id, status) VALUES (3, 'pending');
-- UPDATE products SET stock = stock - 500 WHERE sku = 'P006';
-- COMMIT;

UPDATE orders SET status = 'shipped' WHERE order_id = 2;

CREATE TABLE archived_orders AS SELECT * FROM orders WHERE 1 = 0;
INSERT INTO archived_orders SELECT * FROM orders WHERE status = 'shipped';

ALTER TABLE orders ADD COLUMN discount_pct INT NOT NULL DEFAULT 0 CHECK (discount_pct BETWEEN 0 AND 50);

-- SELECT * FROM customers;
-- SELECT * FROM order_items;
-- SELECT * FROM orders;
-- SELECT * FROM products;
