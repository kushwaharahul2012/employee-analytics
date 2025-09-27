-- Day 6: Data Validation & Referential Integrity
-- Database: employeeanalytics
-- This script adds CHECK constraints to enforce basic data quality rules.

USE employeeanalytics;
GO

-- Salary must always be positive
IF NOT EXISTS (
    SELECT * FROM sys.check_constraints WHERE name = 'CK_salaries_salary'
)
BEGIN
    ALTER TABLE dbo.salaries
    ADD CONSTRAINT CK_salaries_salary CHECK (salary > 0);
END
GO

-- KPI Score must be between 1 and 5
IF NOT EXISTS (
    SELECT * FROM sys.check_constraints WHERE name = 'CK_performance_rating'
)
BEGIN
    ALTER TABLE dbo.performance
    ADD CONSTRAINT CK_performance_rating CHECK (kpi_score BETWEEN 1 AND 5);
END
GO

-- Hire date must be year 2000 or later
IF NOT EXISTS (
    SELECT * FROM sys.check_constraints WHERE name = 'CK_employees_hire_date'
)
BEGIN
    ALTER TABLE dbo.employees
    ADD CONSTRAINT CK_employees_hire_date CHECK (hire_date >= '2000-01-01');
END
GO

-- End of Day 6 constraints
