-- ============================
-- Day 7 EDA SQL Queries
-- Employee Analytics Project
-- ============================

-- 1. Average Salary by Department
SELECT d.department_name, 
       AVG(s.salary) AS avg_salary
FROM dbo.employees e
JOIN dbo.departments d ON e.department_id = d.department_id
JOIN dbo.salaries s ON e.employee_id = s.employee_id
GROUP BY d.department_name
ORDER BY avg_salary DESC;

-- 2. Attrition Count by Department
SELECT d.department_name, 
       COUNT(*) AS attrition_count
FROM dbo.employees_clean ec
JOIN dbo.departments d ON ec.Department = d.department_name
WHERE ec.Attrition = 'Yes'
GROUP BY d.department_name
ORDER BY attrition_count DESC;

-- 3. Top 10 Performers by Salary
SELECT TOP 10 
       e.employee_id, 
       e.first_name, 
       e.last_name, 
       p.kpi_score, 
       s.salary
FROM dbo.employees e
JOIN dbo.performance p ON e.employee_id = p.employee_id
JOIN dbo.salaries s ON e.employee_id = s.employee_id
WHERE p.kpi_score >= 4
ORDER BY s.salary DESC;
