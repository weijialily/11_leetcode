-- # Write your MySQL query statement below
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b 
ON e.empId = b.empId
-- WHERE b.bonus IS NULL OR b.bonus < 1000
WHERE ifnull(b.bonus, 0) <1000; -- faster with ifnull function