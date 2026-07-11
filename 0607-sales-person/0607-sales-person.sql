WITH red_sales AS(
    SELECT DISTINCT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
)
SELECT sp.name
FROM SalesPerson sp
LEFT JOIN red_sales rs ON sp.sales_id = rs.sales_id
WHERE rs.sales_id IS NULL;