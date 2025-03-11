-- ========================
-- 📌 Department Procedures
-- ========================

-- Create Department
CREATE PROCEDURE CreateDepartment @name NVARCHAR(100), @hod_id BIGINT
AS
BEGIN
    INSERT INTO department_154 (name, hod_id) VALUES (@name, @hod_id);
END;
GO

-- Read Department
CREATE PROCEDURE ReadDepartment @dept_id BIGINT
AS
BEGIN
    SELECT * FROM department_154 WHERE id = @dept_id;
END;
GO

-- Update Department
CREATE PROCEDURE UpdateDepartment @dept_id BIGINT, @name NVARCHAR(100), @hod_id BIGINT
AS
BEGIN
    UPDATE department_154 SET name = @name, hod_id = @hod_id WHERE id = @dept_id;
END;
GO

-- Delete Department
CREATE PROCEDURE DeleteDepartment @dept_id BIGINT
AS
BEGIN
    DELETE FROM department_154 WHERE id = @dept_id;
END;
GO

-- List All Departments
CREATE PROCEDURE ListAllDepartments
AS
BEGIN
    SELECT * FROM department_154;
END;
GO


-- =====================
-- 📌 Employee Procedures
-- =====================

-- Create Employee
CREATE PROCEDURE CreateEmployee @phone NVARCHAR(100), @date_of_birth DATE, @gender NVARCHAR(100),
                                @job_position NVARCHAR(100),
                                @date_of_hire DATE, @employee_id NVARCHAR(100), @address NVARCHAR(100),
                                @emergency_contact_name NVARCHAR(100), @emergency_contact_phone NVARCHAR(10),
                                @department_id BIGINT, @user_id BIGINT, @other_names NVARCHAR(100)
AS
BEGIN
    INSERT INTO employee_154 (phone, date_of_birth, gender, job_position, date_of_hire, employee_id, address,
                              emergency_contact_name, emergency_contact_phone, department_id, user_id, other_names)
    VALUES (@phone, @date_of_birth, @gender, @job_position, @date_of_hire, @employee_id, @address,
            @emergency_contact_name, @emergency_contact_phone, @department_id, @user_id, @other_names);
END;
GO

-- Read Employee
CREATE PROCEDURE ReadEmployee @emp_id BIGINT
AS
BEGIN
    SELECT * FROM employee_154 WHERE id = @emp_id;
END;
GO

-- Update Employee
CREATE PROCEDURE UpdateEmployee @emp_id BIGINT, @phone NVARCHAR(100), @job_position NVARCHAR(100),
                                @address NVARCHAR(100)
AS
BEGIN
    UPDATE employee_154 SET phone = @phone, job_position = @job_position, address = @address WHERE id = @emp_id;
END;
GO

-- Delete Employee
CREATE PROCEDURE DeleteEmployee @emp_id BIGINT
AS
BEGIN
    DELETE FROM employee_154 WHERE id = @emp_id;
END;
GO

-- List All Employees
CREATE PROCEDURE ListAllEmployees
AS
BEGIN
    SELECT * FROM employee_154;
END;
GO


-- =====================
-- 📌 Task Procedures
-- =====================

-- Create Task
CREATE PROCEDURE CreateTask @employee_id BIGINT, @title NVARCHAR(255), @description NVARCHAR(MAX),
                            @due_date DATE, @status NVARCHAR(20)
AS
BEGIN
    INSERT INTO task_154 (employee_id, title, description, due_date, status, created_at, updated_at)
    VALUES (@employee_id, @title, @description, @due_date, @status, SYSDATETIMEOFFSET(), SYSDATETIMEOFFSET());
END;
GO

-- Read Task
CREATE PROCEDURE ReadTask @task_id BIGINT
AS
BEGIN
    SELECT * FROM task_154 WHERE id = @task_id;
END;
GO

-- Update Task
CREATE PROCEDURE UpdateTask @task_id BIGINT, @title NVARCHAR(255), @description NVARCHAR(MAX), @status NVARCHAR(20)
AS
BEGIN
    UPDATE task_154
    SET title       = @title,
        description = @description,
        status      = @status,
        updated_at  = SYSDATETIMEOFFSET()
    WHERE id = @task_id;
END;
GO

-- Delete Task
CREATE PROCEDURE DeleteTask @task_id BIGINT
AS
BEGIN
    DELETE FROM task_154 WHERE id = @task_id;
END;
GO

-- List All Tasks
CREATE PROCEDURE ListAllTasks
AS
BEGIN
    SELECT * FROM task_154;
END;
GO


-- =========================
-- 📌 Payroll Procedures
-- =========================

-- Create Payroll Record
CREATE PROCEDURE CreatePayroll @employee_id BIGINT, @basic_salary NUMERIC(10, 2), @bonuses NUMERIC(10, 2),
                               @deductions NUMERIC(10, 2), @net_salary NUMERIC(10, 2), @payment_date DATE,
                               @bank_name NVARCHAR(100), @account_name NVARCHAR(100), @account_number NVARCHAR(100)
AS
BEGIN
    INSERT INTO payroll_154 (employee_id, basic_salary, bonuses, deductions, net_salary, payment_date, bank_name,
                             account_name, account_number)
    VALUES (@employee_id, @basic_salary, @bonuses, @deductions, @net_salary, @payment_date, @bank_name, @account_name,
            @account_number);
END;
GO

-- Read Payroll Record
CREATE PROCEDURE ReadPayroll @payroll_id BIGINT
AS
BEGIN
    SELECT * FROM payroll_154 WHERE id = @payroll_id;
END;
GO

-- Update Payroll Record
CREATE PROCEDURE UpdatePayroll @payroll_id BIGINT, @basic_salary NUMERIC(10, 2), @bonuses NUMERIC(10, 2),
                               @deductions NUMERIC(10, 2)
AS
BEGIN
    UPDATE payroll_154
    SET basic_salary = @basic_salary,
        bonuses      = @bonuses,
        deductions   = @deductions
    WHERE id = @payroll_id;
END;
GO

-- Delete Payroll Record
CREATE PROCEDURE DeletePayroll @payroll_id BIGINT
AS
BEGIN
    DELETE FROM payroll_154 WHERE id = @payroll_id;
END;
GO

-- List All Payroll Records
CREATE PROCEDURE ListAllPayrolls
AS
BEGIN
    SELECT * FROM payroll_154;
END;
GO


-- ===========================
-- 📌 Leave Procedures
-- ===========================

-- Create Leave Record
CREATE PROCEDURE CreateLeave @employee_id BIGINT, @leave_type NVARCHAR(20), @start_date DATE, @end_date DATE,
                             @status NVARCHAR(20)
AS
BEGIN
    INSERT INTO leave_154 (employee_id, leave_type, start_date, end_date, status)
    VALUES (@employee_id, @leave_type, @start_date, @end_date, @status);
END;
GO

-- Read Leave Record
CREATE PROCEDURE ReadLeave @leave_id BIGINT
AS
BEGIN
    SELECT * FROM leave_154 WHERE id = @leave_id;
END;
GO

-- Update Leave Record
CREATE PROCEDURE UpdateLeave @leave_id BIGINT, @status NVARCHAR(20)
AS
BEGIN
    UPDATE leave_154 SET status = @status WHERE id = @leave_id;
END;
GO

-- Delete Leave Record
CREATE PROCEDURE DeleteLeave @leave_id BIGINT
AS
BEGIN
    DELETE FROM leave_154 WHERE id = @leave_id;
END;
GO

-- List All Leave Records
CREATE PROCEDURE ListAllLeaves
AS
BEGIN
    SELECT * FROM leave_154;
END;
GO
