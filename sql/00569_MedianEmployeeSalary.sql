-- # Write your MySQL query statement below
WITH add_rank AS (
    SELECT *,
        ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary) AS rnk
    FROM Employee
)

, add_count AS(
    SELECT 
        COUNT(DISTINCT(id)) AS cnt, 
        company
    FROM Employee
    GROUP BY company
)

SELECT 
    r.id,
    r.company,
    r.salary
FROM add_rank r
JOIN add_count c
ON r.company = c.company
AND r.rnk BETWEEN c.cnt/2 AND c.cnt/2+1
-- # Write your MySQL query statement below
SELECT e.id, e.month,
    SUM(e2.Salary) as Salary
FROM Employee e
JOIN Employee e2 
ON (e.Id = e2.Id AND e.Month >= e2.Month AND (e.Month - e2.Month <= 2))
WHERE e.Month < (SELECT MAX(Month) from Employee where Id = e.Id)
GROUP BY e.Id, e.Month
ORDER BY e.Id, e.Month DESC
