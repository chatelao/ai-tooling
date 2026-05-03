-- Example of a window function
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) as avg_dept_salary
FROM employees;
