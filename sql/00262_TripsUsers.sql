--  Write your MySQL query statement below
WITH trip_status AS(
    SELECT 
        t.request_at AS Day,
        t.status
    FROM Trips t
    JOIN Users u1 ON t.client_id = u1.users_id AND u1.banned = 'No'
    JOIN Users u2 ON t.driver_id = u2.users_id AND u2.banned = 'No'
    WHERE t.request_at BETWEEN "2013-10-01" AND "2013-10-03"
)
SELECT
    Day,
    ROUND(SUM(status != 'completed')/COUNT(status), 2) AS 'Cancellation Rate'
FROM trip_status
GROUP BY Day
