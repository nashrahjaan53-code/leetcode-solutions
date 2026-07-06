# Write your MySQL query statement below
#select name
#from Customer
#WHERE referee_id != 2 OR referee_id IS NULL

#USING COALESCE:
SELECT name
FROM Customer
WHERE COALESCE(referee_id, 0) != 2;