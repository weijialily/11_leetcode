-- https://leetcode.com/problems/combine-two-tables/

-- Write your MySQL query statement below
SELECT p.firstname, p.lastname, a.city, a.state
FROM Person p LEFT JOIN Address a
ON p.personID = a.personID