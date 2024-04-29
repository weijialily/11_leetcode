-- # Write your MySQL query statement below
WITH high_earner AS (
    SELECT 
        name, 
        salary,
        departmentId,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk
    FROM Employee
)

SELECT 
    d.name AS Department,
    h.name AS Employee,
    h.salary AS Salary
FROM high_earner h
JOIN Department d
ON h.departmentId = d.id
WHERE h.rnk <= 3
ORDER BY Department, Salary
