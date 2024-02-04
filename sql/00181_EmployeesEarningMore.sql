-- Write your MySQL query statement below

-- # Use Join: Slower
-- SELECT e1.name AS Employee
-- FROM Employee e1 
-- JOIN Employee e2
-- ON e1.ManagerId = e2.Id AND e1.Salary > e2.Salary

SELECT e1.name AS Employee
FROM Employee e1, Employee e2
WHERE e1.ManagerId = e2.Id AND e1.Salary > e2.Salary