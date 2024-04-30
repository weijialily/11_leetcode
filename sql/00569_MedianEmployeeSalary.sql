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
