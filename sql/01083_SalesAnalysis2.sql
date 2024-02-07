-- # Write your MySQL query statement below
-- 1. 
-- SELECT DISTINCT s.buyer_id 
-- FROM Sales s
-- JOIN Product p
-- ON s.product_id = p.product_id
-- AND p.product_name = 'S8'
-- AND s.buyer_id NOT IN
-- (
--     SELECT DISTINCT s.buyer_id 
--     FROM Sales s
--     JOIN Product p
--     ON s.product_id = p.product_id
--     AND p.product_name = 'iPhone'
-- ) 

-- 2. Use LEFT JOIN
-- SELECT DISTINCT s.buyer_id
-- FROM Sales s
-- JOIN Product p
-- ON s.product_id = p.product_id
-- AND p.product_name = 'S8'
-- LEFT JOIN
-- (
--     SELECT DISTINCT buyer_id
--     FROM Sales s
--     JOIN Product p
--     ON s.product_id = p.product_id
--     AND p.product_name = 'iPhone'
-- ) a
-- ON s.buyer_id = a.buyer_id
-- WHERE a.buyer_id IS NULL

-- 3. Use CASE WHEN
-- SELECT DISTINCT s.buyer_id
-- FROM Sales s
-- JOIN Product p
-- ON s.product_id = p.product_id
-- GROUP BY s.buyer_id
-- HAVING SUM(CASE WHEN p.product_name = 'iPHONE' THEN 1 ELSE 0 END) = 0
-- AND SUM(CASE WHEN p.product_name = 'S8' THEN 1 ELSE 0 END) > 0

-- 4. Use GROUP_CONCAT
SELECT DISTINCT s.buyer_id
FROM Sales s
JOIN Product p
ON s.product_id = p.product_id
GROUP BY s.buyer_id
HAVING GROUP_CONCAT(p.product_name) LIKE '%S8%'
AND GROUP_CONCAT(p.product_name) NOT LIKE '%iPhone%' 