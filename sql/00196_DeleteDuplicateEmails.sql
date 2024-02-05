-- # Write your MySQL query statement below
DELETE p1 
FROM person p1, person p2 
WHERE p1.email = p2.email AND p1.Id > p2.Id

-- # Slower solution
-- DELETE FROM Person WHERE Id NOT IN
-- (
--     SELECT * FROM 
--     (
--         SELECT MIN(Id) FROM person
--         GROUP BY email
--     ) AS p
-- )