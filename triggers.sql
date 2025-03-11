CREATE TABLE audit_log_154
(
    id          BIGINT IDENTITY PRIMARY KEY,
    table_name  NVARCHAR(100) NOT NULL,
    action_type NVARCHAR(10)  NOT NULL, -- INSERT, UPDATE, DELETE
    action_time DATETIMEOFFSET DEFAULT SYSDATETIMEOFFSET(),
    record_id   BIGINT        NOT NULL  -- The ID of the affected row
);
GO

CREATE TRIGGER trg_insert_employee
    ON employee_154
    AFTER INSERT
    AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'employee_154', 'INSERT', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_update_employee
    ON employee_154
    AFTER UPDATE
    AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'employee_154', 'UPDATE', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_delete_employee
    ON employee_154
    AFTER DELETE
    AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'employee_154', 'DELETE', id
    FROM deleted;
END;
GO


-- Create Audit Log Table
CREATE TABLE audit_log_154
(
    id          BIGINT IDENTITY PRIMARY KEY,
    table_name  NVARCHAR(100) NOT NULL,
    action_type NVARCHAR(10)  NOT NULL, -- INSERT, UPDATE, DELETE
    action_time DATETIMEOFFSET DEFAULT SYSDATETIMEOFFSET(),
    record_id   BIGINT        NOT NULL  -- The ID of the affected row
);
GO

-- Triggers for attendance_154
CREATE TRIGGER trg_insert_attendance
    ON attendance_154
    AFTER INSERT AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'attendance_154', 'INSERT', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_update_attendance
    ON attendance_154
    AFTER UPDATE AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'attendance_154', 'UPDATE', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_delete_attendance
    ON attendance_154
    AFTER DELETE AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'attendance_154', 'DELETE', id
    FROM deleted;
END;
GO

-- Triggers for department_154
CREATE TRIGGER trg_insert_department
    ON department_154
    AFTER INSERT AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'department_154', 'INSERT', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_update_department
    ON department_154
    AFTER UPDATE AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'department_154', 'UPDATE', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_delete_department
    ON department_154
    AFTER DELETE AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'department_154', 'DELETE', id
    FROM deleted;
END;
GO

-- Triggers for employee_154
CREATE TRIGGER trg_insert_employee
    ON employee_154
    AFTER INSERT AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'employee_154', 'INSERT', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_update_employee
    ON employee_154
    AFTER UPDATE AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'employee_154', 'UPDATE', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_delete_employee
    ON employee_154
    AFTER DELETE AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'employee_154', 'DELETE', id
    FROM deleted;
END;
GO

-- Triggers for leave_154
CREATE TRIGGER trg_insert_leave
    ON leave_154
    AFTER INSERT AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'leave_154', 'INSERT', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_update_leave
    ON leave_154
    AFTER UPDATE AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'leave_154', 'UPDATE', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_delete_leave
    ON leave_154
    AFTER DELETE AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'leave_154', 'DELETE', id
    FROM deleted;
END;
GO

-- Triggers for payroll_154
CREATE TRIGGER trg_insert_payroll
    ON payroll_154
    AFTER INSERT AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'payroll_154', 'INSERT', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_update_payroll
    ON payroll_154
    AFTER UPDATE AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'payroll_154', 'UPDATE', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_delete_payroll
    ON payroll_154
    AFTER DELETE AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'payroll_154', 'DELETE', id
    FROM deleted;
END;
GO

-- Triggers for notification_154
CREATE TRIGGER trg_insert_notification
    ON notification_154
    AFTER INSERT AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'notification_154', 'INSERT', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_update_notification
    ON notification_154
    AFTER UPDATE AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'notification_154', 'UPDATE', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_delete_notification
    ON notification_154
    AFTER DELETE AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'notification_154', 'DELETE', id
    FROM deleted;
END;
GO

-- Triggers for task_154
CREATE TRIGGER trg_insert_task
    ON task_154
    AFTER INSERT AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'task_154', 'INSERT', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_update_task
    ON task_154
    AFTER UPDATE AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'task_154', 'UPDATE', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_delete_task
    ON task_154
    AFTER DELETE AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'task_154', 'DELETE', id
    FROM deleted;
END;
GO

-- Triggers for core_customuser
CREATE TRIGGER trg_insert_user
    ON core_customuser
    AFTER INSERT AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'core_customuser', 'INSERT', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_update_user
    ON core_customuser
    AFTER UPDATE AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'core_customuser', 'UPDATE', id
    FROM inserted;
END;
GO

CREATE TRIGGER trg_delete_user
    ON core_customuser
    AFTER DELETE AS
BEGIN
    INSERT INTO audit_log_154 (table_name, action_type, record_id)
    SELECT 'core_customuser', 'DELETE', id
    FROM deleted;
END;
GO
