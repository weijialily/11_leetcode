-- # Write your MySQL query statement below
WITH Post AS(
    SELECT DISTINCT sub_id AS post_id
    FROM Submissions
    WHERE parent_id IS NULL
)
SELECT 
    Post.post_id,
    COUNT(DISTINCT Submissions.sub_id) AS number_of_comments
FROM Post
LEFT JOIN Submissions
ON Post.post_id = Submissions.parent_id
GROUP BY Post.post_id
ORDER BY Post.post_id ASC
