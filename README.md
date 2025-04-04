# Employee Management System (EMS)

## Overview

The Employee Management System (EMS) is a web-based application designed to manage employee records, attendance, and departments within an organization. The system provides role-based access control, allowing different levels of access and functionality for Admins, HR Managers, Heads of Departments (HODs), and regular employees.

## Features

- **Employee Management**: Create, update, and delete employee records.
- **Attendance Management**: Check-in and check-out functionality for employees.
- **Department Management**: Create, update, and delete departments.
- **Role-Based Access Control**: Different functionalities based on user roles.
- **Profile Management**: Employees can update their profiles.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (default for Django)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/keyy-tech/ems.git
    cd ems
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

7. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage

### Employee Management

- **Add Employee**: Navigate to the employee list and click on "Add Employee".
- **Edit Employee**: Click on the "Edit" button next to an employee's record.
- **Delete Employee**: Click on the "Delete" button next to an employee's record and confirm the deletion.

### Attendance Management

- **Check-In**: Employees can check in by navigating to the check-in page.
- **Check-Out**: Employees can check out by navigating to the check-out page.

### Department Management

- **Add Department**: Navigate to the department list and click on "Add Department".
- **Edit Department**: Click on the "Edit" button next to a department's record.
- **Delete Department**: Click on the "Delete" button next to a department's record and confirm the deletion.

### Profile Management

- **Update Profile**: Employees can update their profile information by navigating to the profile page.

## Contributing

1. **Fork the repository**.
2. **Create a new branch**:
    ```sh
    git checkout -b feature/your-feature-name
    ```
3. **Make your changes**.
4. **Commit your changes**:
    ```sh
    git commit -m "Add your commit message"
    ```
5. **Push to the branch**:
    ```sh
    git push origin feature/your-feature-name
    ```
6. **Create a pull request**.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any inquiries or issues, please contact [keyy-tech](https://github.com/keyy-tech).