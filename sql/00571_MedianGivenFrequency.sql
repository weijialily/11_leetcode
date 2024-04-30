-- # Write your MySQL query statement below
WITH freq AS (
    SELECT
        *,
        SUM(frequency) OVER (ORDER BY num ASC) AS accumulated_sum,
        SUM(frequency) OVER ()/2 AS medium_sum
    FROM Numbers
)

SELECT
    ROUND(AVG(num*1.0), 2) AS Median
FROM freq
WHERE accumulated_sum - frequency <= medium_sum
AND accumulated_sum >= medium_sum
