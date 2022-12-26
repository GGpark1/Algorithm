# # Write your MySQL query statement below
SELECT D.name AS 'Department', E.name AS 'Employee', E.salary AS 'Salary'
FROM Employee E
INNER JOIN Department D ON E.departmentId = D.id 
WHERE (E.salary, D.name) IN (
    SELECT max(E.salary) AS max_salary, D.name AS Department
    FROM Employee E
    INNER JOIN Department D ON E.departmentId = D.id
    GROUP BY D.name)