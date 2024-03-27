-- # Write your MySQL query statement below
SELECT p.product_name, SUM(o.unit) AS unit
FROM Orders o
LEFT JOIN Products p
-- ON o.product_id = p.product_id AND o.order_date >= '2020-02-01' AND o.order_date <= '2020-02-29'
-- ON o.product_id = p.product_id AND YEAR(o.order_date) = '2020' AND MONTH(o.order_date) = '02'
ON o.product_id = p.product_id
WHERE YEAR(o.order_date) = '2020' AND MONTH(o.order_date) = '02'
GROUP BY p.product_name
HAVING unit >= 100 AND product_name IS NOT NULL