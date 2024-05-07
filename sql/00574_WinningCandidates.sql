-- # Write your MySQL query statement below
-- SELECT c.name
-- FROM Candidate c
-- JOIN (
--     SELECT 
--         candidateId,
--         COUNT(candidateId) AS vote_count
--     FROM Vote
--     GROUP BY candidateId
--     ORDER BY vote_count DESC
--     LIMIT 1
-- ) AS w
-- ON c.id = w.candidateId

WITH vote_count_table AS (
    SELECT 
    candidateId,
    RANK() OVER (ORDER BY COUNT(candidateId) DESC) AS vote_rank
    FROM Vote
    GROUP BY candidateId
)

SELECT c.name
FROM Candidate c
JOIN (
    SELECT candidateId
    FROM vote_count_table
    WHERE vote_rank = 1
) AS w
ON c.id = w.candidateId
