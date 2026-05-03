-- Example of aggregate functions
SELECT category, COUNT(*), AVG(price), SUM(stock)
FROM products
GROUP BY category
HAVING COUNT(*) > 5;
