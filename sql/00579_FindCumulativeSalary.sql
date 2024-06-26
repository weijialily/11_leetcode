-- # Write your MySQL query statement below
SELECT e.id, e.month,
    SUM(e2.Salary) as Salary
FROM Employee e
JOIN Employee e2 
ON (e.Id = e2.Id AND e.Month >= e2.Month AND (e.Month - e2.Month <= 2))
WHERE e.Month < (SELECT MAX(Month) from Employee where Id = e.Id)
GROUP BY e.Id, e.Month
ORDER BY e.Id, e.Month DESC
