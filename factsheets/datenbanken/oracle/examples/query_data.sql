SELECT FirstName, LastName, HireDate
FROM Employees
WHERE HireDate >= TRUNC(SYSDATE, 'YYYY');
