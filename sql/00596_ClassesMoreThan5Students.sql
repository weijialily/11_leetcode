-- # Write your MySQL query statement below
SELECT class
FROM Courses
GROUP by class
HAVING COUNT(student) >= 5