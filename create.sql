-- Attendance
create table attendance_154
(
    id                  bigint identity primary key,
    date                date not null,
    check_in_time       time,
    check_out_time      time,
    total_working_hours numeric(5, 2),
    employee_id         bigint not null
        constraint attendance_attendance_employee_id_63b4db5a_fk_employee_154_id
            references employee_154
)
go

create index attendance_attendance_employee_id_63b4db5a
    on attendance_154 (employee_id)
go

-- Department
create table department_154
(
    id     bigint identity primary key,
    name   nvarchar(100) not null,
    hod_id bigint
        constraint department_154_hod_id_dc70fa9d_fk_employee_154_id
            references employee_154
)
go

create index department_154_hod_id_dc70fa9d
    on department_154 (hod_id)
go

-- Employee
create table employee_154
(
    id                      bigint identity primary key,
    phone                   nvarchar(100) not null,
    date_of_birth           date not null,
    gender                  nvarchar(100) not null,
    job_position            nvarchar(100) not null,
    date_of_hire            date not null,
    employee_id             nvarchar(100) not null,
    address                 nvarchar(100) not null,
    emergency_contact_name  nvarchar(100) not null,
    emergency_contact_phone nvarchar(10) not null,
    department_id           bigint
        constraint employee_154_department_id_1d1da763_fk_department_154_id
            references department_154,
    user_id                 bigint not null unique
        constraint employee_154_user_id_1d99086f_fk_core_customuser_id
            references core_customuser,
    other_names             nvarchar(100)
)
go

create index employee_154_department_id_1d1da763
    on employee_154 (department_id)
go

-- Leave
create table leave_154
(
    id          bigint identity primary key,
    leave_type  nvarchar(20) not null,
    start_date  date not null,
    end_date    date not null,
    status      nvarchar(20) not null,
    employee_id bigint not null
        constraint leave_154_employee_id_cb07ab82_fk_employee_154_id
            references employee_154
)
go

create index leave_154_employee_id_cb07ab82
    on leave_154 (employee_id)
go

-- Payroll
create table payroll_154
(
    id              bigint identity primary key,
    basic_salary    numeric(10, 2) not null,
    bonuses         numeric(10, 2) default 0.00,
    deductions      numeric(10, 2) default 0.00,
    net_salary      numeric(10, 2),
    payment_date    date not null,
    bank_name       nvarchar(100) not null,
    account_name    nvarchar(100) not null,
    account_number  nvarchar(100) not null,
    employee_id     bigint not null
        constraint payroll_154_employee_id_fk
            references employee_154
)
go

create index payroll_154_employee_id_idx
    on payroll_154 (employee_id)
go

-- Notification
create table notification_154
(
    id          bigint identity primary key,
    message     nvarchar(max) not null,
    created_at  datetimeoffset not null,
    employee_id bigint not null
        constraint notification_154_employee_id_5214d0dd_fk_employee_154_id
            references employee_154
)
go

create index notification_154_employee_id_5214d0dd
    on notification_154 (employee_id)
go

-- Task
create table task_154
(
    id          bigint identity primary key,
    title       nvarchar(255) not null,
    description nvarchar(max),
    due_date    date not null,
    status      nvarchar(20) not null,
    created_at  datetimeoffset not null,
    updated_at  datetimeoffset not null,
    employee_id bigint not null
        constraint task_154_employee_id_646b76c7_fk_employee_154_id
            references employee_154
)
go

create index task_154_employee_id_646b76c7
    on task_154 (employee_id)
go

-- User
create table core_customuser
(
    id           bigint identity primary key,
    password     nvarchar(128) not null,
    last_login   datetimeoffset,
    is_superuser bit not null,
    username     nvarchar(150) not null unique,
    first_name   nvarchar(150) not null,
    last_name    nvarchar(150) not null,
    email        nvarchar(254) not null,
    is_staff     bit not null,
    is_active    bit not null,
    date_joined  datetimeoffset not null,
    role         nvarchar(20) not null
)
go