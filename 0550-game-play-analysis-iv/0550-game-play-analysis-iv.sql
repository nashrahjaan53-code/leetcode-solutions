# Write your MySQL query statement below
WITH player_dates AS (
    SELECT 
        player_id,
        event_date,
        ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS rn,
        LEAD(event_date) OVER (PARTITION BY player_id ORDER BY event_date) AS next_date
    FROM Activity
)
SELECT 
    ROUND(
        SUM(CASE 
            WHEN rn = 1 AND next_date = DATE_ADD(event_date, INTERVAL 1 DAY) 
            THEN 1 ELSE 0 
        END) / COUNT(DISTINCT player_id), 
        2
    ) AS fraction
FROM player_dates;