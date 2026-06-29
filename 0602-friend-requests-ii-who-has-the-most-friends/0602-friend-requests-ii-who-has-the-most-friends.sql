WITH friend_counts AS (
    SELECT id, COUNT(*) AS num
    FROM (
        SELECT requester_id AS id FROM RequestAccepted
        UNION ALL
        SELECT accepter_id AS id FROM RequestAccepted
    ) AS friends
    GROUP BY id
)
SELECT id, num
FROM friend_counts
WHERE num = (SELECT MAX(num) FROM friend_counts);
