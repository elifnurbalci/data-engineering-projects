-- SELECT * FROM sales
-- SELECT * FROM products
-- SELECT * FROM users
-- SELECT * FROM categories


-- What are the top three products by **number of items sold**?

SELECT p.title, COUNT(*) AS total_items_sold
FROM sales s
JOIN products p ON s."productId" = p.id
GROUP BY p.title
ORDER BY total_items_sold DESC
LIMIT 3;


-- What are the top three products by **monetary value**?

SELECT p.title, SUM(p.cost) AS total_sales_value
FROM sales s
JOIN products p ON s."productId" = p.id
GROUP BY p.title
ORDER BY total_sales_value DESC
LIMIT 3;

-- Which user was the top spender in December 2022? Provide their email address and phone number.

SELECT u.email, u.phone_number, SUM(p.cost) AS total_spent
FROM sales s
JOIN users u ON s."buyerId" = u.id
JOIN products p ON s."productId" = p.id
WHERE s.transaction_ts >= '2022-12-01' AND s.transaction_ts < '2023-01-01'
GROUP BY u.email, u.phone_number
ORDER BY total_spent DESC
LIMIT 1;