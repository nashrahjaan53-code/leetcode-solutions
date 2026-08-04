SELECT MAX(num) AS num
FROM(
    SELECT num
    FROM MyNumbers
    Group By num
    Having COUNT(*) = 1
) AS single_numbers;

