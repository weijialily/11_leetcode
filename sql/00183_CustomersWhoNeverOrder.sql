-- Write your MySQL query statement below

-- Use LEFT JOIN
-- SELECT c.name AS Customers
-- FROM Customers c
-- LEFT JOIN Orders o 
-- ON c.id = o.customerId
-- WHERE o.id is NULL

SELECT name AS Customers
FROM Customers
WHERE customers.id NOT IN
(
    SELECT customerid FROM Orders
)