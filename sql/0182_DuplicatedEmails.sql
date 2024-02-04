# Write your MySQL query statement below
# Use Having: Slower
-- SELECT email AS Email
-- FROM Person
-- GROUP BY email
-- HAVING count(email) > 1

SELECT Email
FROM
    (
        SELECT email AS Email, count(Email) AS num
        FROM Person
        GROUP BY Email
    ) AS statistic
WHERE num > 1
