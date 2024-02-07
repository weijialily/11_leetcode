-- # Write your MySQL query statement below
-- SELECT seller_id 
-- FROM Sales
-- GROUP BY seller_id
-- HAVING SUM(price) = (
--     SELECT MAX(total_sales.total_sales_price) FROM (
--         SELECT SUM(price) AS total_sales_price
--         FROM Sales s
--         GROUP BY seller_id
--     ) AS total_sales
-- )

-- Use WITH
WITH total_sales AS (
    SELECT seller_id, SUM(price) AS total_prices
    FROM Sales
    GROUP BY seller_id
)
SELECT seller_id
FROM total_sales
WHERE total_prices = (
    SELECT MAX(total_prices)
    FROM total_sales
)