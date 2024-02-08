-- # Write your MySQL query statement below
-- SELECT player_id, device_id
-- FROM Activity
-- WHERE (player_id, event_date) IN (
--     SELECT player_id, MIN(event_date)
--     FROM Activity
--     GROUP BY player_id
-- )

WITH min_date AS (
    SELECT player_id, MIN(event_date) AS event_date
    FROM Activity 
    GROUP BY player_id
)
SELECT A.player_id, A.device_id
FROM Activity A
INNER JOIN min_date M 
ON M.player_id = A.player_id AND M.event_date = A.event_date