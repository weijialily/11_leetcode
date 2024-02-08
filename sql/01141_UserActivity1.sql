-- # Write your MySQL query statement below
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date <= '2019-07-27' AND activity_date >= '2019-06-28'
-- activity_date BETWEEN '2019-06-28' AND '2019-07-27'
-- DATEDIFF('2019-07-27', activity_date)<30 AND DATEDIFF('2019-07-27', activity_date)>=0 
GROUP BY activity_date
