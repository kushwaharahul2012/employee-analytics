-- Day 5: Normalize employees/salaries/performance tables
-- Database: employeeanalytics
-- This script creates normalized tables and populates them from employees_clean.

USE employeeanalytics;
GO

-- Create departments table
IF OBJECT_ID('dbo.departments','U') IS NULL
BEGIN
    CREATE TABLE dbo.departments (
        department_id INT PRIMARY KEY,
        department_name VARCHAR(150) NOT NULL
    );
END
GO

-- Create employees table
IF OBJECT_ID('dbo.employees','U') IS NULL
BEGIN
    CREATE TABLE dbo.employees (
        employee_id INT PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        department_id INT,
        hire_date DATE,
        email VARCHAR(150),
        CONSTRAINT FK_employees_departments FOREIGN KEY (department_id)
            REFERENCES dbo.departments(department_id)
    );
END
GO

-- Create salaries table
IF OBJECT_ID('dbo.salaries','U') IS NULL
BEGIN
    CREATE TABLE dbo.salaries (
        salary_id INT IDENTITY(1,1) PRIMARY KEY,
        employee_id INT NOT NULL,
        salary DECIMAL(18,2),
        effective_date DATE,
        CONSTRAINT FK_salaries_employees FOREIGN KEY (employee_id)
            REFERENCES dbo.employees(employee_id)
    );
END
GO

-- Create performance table
IF OBJECT_ID('dbo.performance','U') IS NULL
BEGIN
    CREATE TABLE dbo.performance (
        performance_id INT IDENTITY(1,1) PRIMARY KEY,
        employee_id INT NOT NULL,
        kpi_score DECIMAL(6,2),
        review_date DATE,
        CONSTRAINT FK_performance_employees FOREIGN KEY (employee_id)
            REFERENCES dbo.employees(employee_id)
    );
END
GO

-- Populate departments (auto-generate department_id)
INSERT INTO dbo.departments (department_id, department_name)
SELECT ROW_NUMBER() OVER (ORDER BY Department) + 1000 AS department_id,
       Department
FROM (SELECT DISTINCT Department FROM dbo.employees_clean WHERE Department IS NOT NULL) t
WHERE NOT EXISTS (
    SELECT 1 FROM dbo.departments d WHERE d.department_name = t.Department
);

-- Populate employees
INSERT INTO dbo.employees (employee_id, first_name, last_name, department_id, hire_date, email)
SELECT DISTINCT ec.EmployeeID,
       ec.Name,              -- stored in first_name column
       NULL,                 -- no last name column available
       d.department_id,
       CAST(ec.JoinYear AS VARCHAR(4)) + '-01-01', -- hire_date from JoinYear
       NULL                  -- no email in dataset
FROM dbo.employees_clean ec
LEFT JOIN dbo.departments d ON ec.Department = d.department_name
WHERE NOT EXISTS (
    SELECT 1 FROM dbo.employees e WHERE e.employee_id = ec.EmployeeID
);

-- Populate salaries
INSERT INTO dbo.salaries (employee_id, salary, effective_date)
SELECT ec.EmployeeID,
       ec.Salary,
       CAST(ec.JoinYear AS VARCHAR(4)) + '-01-01'
FROM dbo.employees_clean ec
WHERE ec.Salary IS NOT NULL
  AND NOT EXISTS (
      SELECT 1 FROM dbo.salaries s
      WHERE s.employee_id = ec.EmployeeID
        AND s.salary = ec.Salary
        AND s.effective_date = CAST(ec.JoinYear AS VARCHAR(4)) + '-01-01'
  );

-- Populate performance
INSERT INTO dbo.performance (employee_id, kpi_score, review_date)
SELECT ec.EmployeeID,
       ec.PerformanceRating,
       CAST(ec.JoinYear AS VARCHAR(4)) + '-12-31'
FROM dbo.employees_clean ec
WHERE ec.PerformanceRating IS NOT NULL
  AND NOT EXISTS (
      SELECT 1 FROM dbo.performance p
      WHERE p.employee_id = ec.EmployeeID
        AND p.kpi_score = ec.PerformanceRating
        AND p.review_date = CAST(ec.JoinYear AS VARCHAR(4)) + '-12-31'
  );

-- Create view for analysis
CREATE OR ALTER VIEW dbo.vw_employee_analysis AS
SELECT 
    e.employee_id,
    e.first_name,
    d.department_name,
    s.salary,
    p.kpi_score
FROM dbo.employees e
INNER JOIN dbo.departments d ON e.department_id = d.department_id
INNER JOIN dbo.salaries s ON e.employee_id = s.employee_id
INNER JOIN dbo.performance p ON e.employee_id = p.employee_id;
GO

-- End of Day 5 normalization
