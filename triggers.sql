-- Create Audit Log Table
CREATE TABLE audit_log_154 (
    id BIGINT IDENTITY PRIMARY KEY,
    action NVARCHAR(50) NOT NULL,
    table_name NVARCHAR(100) NOT NULL,
    employee_id BIGINT NOT NULL,
    changed_data NVARCHAR(MAX),
    action_timestamp DATETIMEOFFSET DEFAULT SYSDATETIME(),
    performed_by NVARCHAR(150) NOT NULL
);
GO

-- Trigger for INSERT on employee_154
CREATE TRIGGER trg_employee_insert
ON employee_154
AFTER INSERT
AS
BEGIN
    INSERT INTO audit_log_154 (action, table_name, employee_id, changed_data, performed_by)
    SELECT 'INSERT', 'employee_154', id, CONCAT('New Employee: ', employee_id), SUSER_NAME()
    FROM inserted;
END;
GO

-- Trigger for UPDATE on employee_154
CREATE TRIGGER trg_employee_update
ON employee_154
AFTER UPDATE
AS
BEGIN
    INSERT INTO audit_log_154 (action, table_name, employee_id, changed_data, performed_by)
    SELECT 'UPDATE', 'employee_154', id, CONCAT('Updated Employee: ', employee_id), SUSER_NAME()
    FROM inserted;
END;
GO

-- Trigger for DELETE on employee_154
CREATE TRIGGER trg_employee_delete
ON employee_154
AFTER DELETE
AS
BEGIN
    INSERT INTO audit_log_154 (action, table_name, employee_id, changed_data, performed_by)
    SELECT 'DELETE', 'employee_154', id, CONCAT('Deleted Employee: ', employee_id), SUSER_NAME()
    FROM deleted;
END;
GO

-- Create User Activity Log Table
CREATE TABLE user_activity_log_154 (
    id BIGINT IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL,
    action NVARCHAR(50) NOT NULL,
    action_timestamp DATETIMEOFFSET DEFAULT SYSDATETIME(),
    performed_by NVARCHAR(150) NOT NULL
);
GO

-- Trigger for Login and Logout (Assuming a Table "user_sessions_154" Tracks Logins)
CREATE TRIGGER trg_user_login_logout
ON core_customuser
AFTER UPDATE
AS
BEGIN
    INSERT INTO user_activity_log_154 (user_id, action, performed_by)
    SELECT id, 
           CASE 
               WHEN is_active = 1 THEN 'LOGIN'
               WHEN is_active = 0 THEN 'LOGOUT'
           END,
           SUSER_NAME()
    FROM inserted;
END;
GO
