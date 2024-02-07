-- # Write your MySQL query statement below
SELECT project_id
FROM Project
GROUP BY project_id
HAVING COUNT(employee_id) = (
    SELECT MAX(p.employees_per_project)
    FROM(
        SELECT COUNT(employee_id) AS employees_per_project
        FROM Project
        GROUP BY project_id
    ) AS p
)