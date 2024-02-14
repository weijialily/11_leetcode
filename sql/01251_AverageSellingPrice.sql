-- # Write your MySQL query statement below

WITH CTE AS (
    SELECT 
        p.product_id,
        CASE WHEN u.purchase_date BETWEEN p.start_date AND p.end_date
        THEN units * price
        END AS total_price,
        units
    FROM Prices p
    LEFT JOIN UnitsSold u
    ON p.product_id = u.product_id
    HAVING total_price IS NOT NULL
)

SELECT 
    p.product_id,
    ROUND(IFNULL(SUM(total_price)/SUM(units), 0),2) AS average_price
FROM Prices AS p
LEFT JOIN CTE 
ON p.product_id = CTE.product_id
GROUP BY product_id;