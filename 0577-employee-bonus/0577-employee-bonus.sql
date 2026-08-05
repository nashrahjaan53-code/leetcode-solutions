
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE CASE 
    WHEN b.bonus IS NULL THEN 1
        WHEN b.bonus < 1000 THEN 1
            ELSE 0
            END = 1; 
