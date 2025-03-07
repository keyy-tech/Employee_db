-- Stored Procedure to Create a Department
CREATE PROCEDURE CreateDepartment @name NVARCHAR(100),
                                  @hod_id BIGINT
AS
BEGIN
    INSERT INTO department_154 (name, hod_id)
    VALUES (@name, @hod_id);
END
GO


-- Create Task
CREATE PROCEDURE CreateTask @employee_id BIGINT,
                            @title NVARCHAR(255),
                            @description NVARCHAR(MAX),
                            @due_date DATE,
                            @status NVARCHAR(20)
AS
BEGIN
    INSERT INTO task_154 (employee_id, title, description, due_date, status, created_at, updated_at)
    VALUES (@employee_id, @title, @description, @due_date, @status, SYSDATETIMEOFFSET(), SYSDATETIMEOFFSET());
END
GO

-- Read Task
CREATE PROCEDURE ReadTask @task_id BIGINT
AS
BEGIN
    SELECT * FROM task_154 WHERE id = @task_id;
END
GO

-- Update Task
CREATE PROCEDURE UpdateTask @task_id BIGINT,
                            @employee_id BIGINT,
                            @title NVARCHAR(255),
                            @description NVARCHAR(MAX),
                            @due_date DATE,
                            @status NVARCHAR(20)
AS
BEGIN
    UPDATE task_154
    SET employee_id = @employee_id,
        title       = @title,
        description = @description,
        due_date    = @due_date,
        status      = @status,
        updated_at  = SYSDATETIMEOFFSET()
    WHERE id = @task_id;
END
GO

-- Delete Task
CREATE PROCEDURE DeleteTask @task_id BIGINT
AS
BEGIN
    DELETE FROM task_154 WHERE id = @task_id;
END
GO

-- List All Tasks
CREATE PROCEDURE ListAllTasks
AS
BEGIN
    SELECT * FROM task_154;
END
GO