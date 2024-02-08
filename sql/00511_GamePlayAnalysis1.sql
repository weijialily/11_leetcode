-- # Write your MySQL query statement below
-- SELECT player_id, MIN(event_date) AS first_login
-- FROM Activity
-- GROUP BY player_id

-- Window functions
SELECT DISTINCT A.player_id, FIRST_VALUE(A.event_date) OVER (
        PARTITION BY A.player_id
        ORDER BY A.event_date
    ) AS first_login
FROM Activity A