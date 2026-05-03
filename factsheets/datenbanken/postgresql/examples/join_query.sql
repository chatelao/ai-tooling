-- Example of a JOIN query
SELECT users.username, orders.order_date, orders.amount
FROM users
JOIN orders ON users.id = orders.user_id
WHERE orders.amount > 100;
