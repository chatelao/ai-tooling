DECLARE
    v_count NUMBER;
BEGIN
    SELECT COUNT(*) INTO v_count FROM Employees;
    DBMS_OUTPUT.PUT_LINE('Total Employees: ' || v_count);
END;
/
