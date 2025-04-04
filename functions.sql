-- Function 1: Calculate Total Hours Worked by an Employee
CREATE FUNCTION dbo.GetTotalWorkingHours(@EmpID BIGINT, @Date DATE)
RETURNS DECIMAL(10,2)
AS
BEGIN
    DECLARE @TotalHours DECIMAL(10,2);
    SELECT @TotalHours = SUM(COALESCE(total_working_hours, 0))
    FROM attendance_154
    WHERE employee_id = @EmpID AND date = @Date;
    RETURN @TotalHours;
END;
GO

-- Function 2: Get Employee Full Name
CREATE FUNCTION dbo.GetEmployeeFullName(@UserID BIGINT)
RETURNS NVARCHAR(300)
AS
BEGIN
    DECLARE @FullName NVARCHAR(300);
    SELECT @FullName = first_name + ' ' + last_name FROM core_customuser WHERE id = @UserID;
    RETURN @FullName;
END;
GO

-- Function 3: Calculate Employee Leave Days Taken
CREATE FUNCTION dbo.GetTotalLeaveDays(@EmpID BIGINT)
RETURNS INT
AS
BEGIN
    DECLARE @TotalDays INT;
    SELECT @TotalDays = SUM(DATEDIFF(DAY, start_date, end_date))
    FROM leave_154
    WHERE employee_id = @EmpID;
    RETURN @TotalDays;
END;
GO

-- Function 4: Calculate Net Salary for an Employee
CREATE FUNCTION dbo.CalculateNetSalary(@EmpID BIGINT)
RETURNS DECIMAL(10,2)
AS
BEGIN
    DECLARE @NetSalary DECIMAL(10,2);
    SELECT @NetSalary = (basic_salary + COALESCE(bonuses, 0) - COALESCE(deductions, 0))
    FROM payroll_154
    WHERE employee_id = @EmpID;
    RETURN @NetSalary;
END;
GO

-- Function 5: Get Pending Tasks Count for an Employee
CREATE FUNCTION dbo.GetPendingTasks(@EmpID BIGINT)
RETURNS INT
AS
BEGIN
    DECLARE @PendingTasks INT;
    SELECT @PendingTasks = COUNT(*)
    FROM task_154
    WHERE employee_id = @EmpID AND status = 'Pending';
    RETURN @PendingTasks;
END;
GO