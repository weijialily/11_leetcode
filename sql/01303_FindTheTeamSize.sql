-- # Write your MySQL query statement below
-- SELECT employee_id, team_size
-- FROM Employee e
-- LEFT JOIN ( 
--     SELECT team_id, COUNT(DISTINCT(employee_id)) AS team_size
--     FROM Employee
--     GROUP BY team_id) AS t
-- ON e.team_id = t.team_id

SELECT employee_id, COUNT(team_id) OVER (PARTITION BY team_id) team_size
FROM Employee
