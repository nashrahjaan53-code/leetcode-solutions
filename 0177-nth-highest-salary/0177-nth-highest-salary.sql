CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
   SET n = n - 1;
  RETURN (
      SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET n
  );
END