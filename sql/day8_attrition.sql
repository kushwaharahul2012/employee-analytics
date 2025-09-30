-- ============================
-- Day 8: Attrition Analysis
-- ============================

-- 1. Attrition % by Department
SELECT d.department_name,
       SUM(CASE WHEN ec.Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS attrition_rate
FROM dbo.employees_clean ec
JOIN dbo.departments d ON ec.Department = d.department_name
GROUP BY d.department_name
ORDER BY attrition_rate DESC;

-- 2. Attrition % by Gender
SELECT ec.Gender,
       SUM(CASE WHEN ec.Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS attrition_rate
FROM dbo.employees_clean ec
GROUP BY ec.Gender;

-- 3. Attrition by Age Group
SELECT 
    CASE 
        WHEN ec.Age BETWEEN 20 AND 29 THEN '20-29'
        WHEN ec.Age BETWEEN 30 AND 39 THEN '30-39'
        WHEN ec.Age BETWEEN 40 AND 49 THEN '40-49'
        ELSE '50+'
    END AS age_group,
    SUM(CASE WHEN ec.Attrition = 'Yes' THEN 1 ELSE 0 END) AS attrition_count,
    COUNT(*) AS total_count,
    SUM(CASE WHEN ec.Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS attrition_rate
FROM dbo.employees_clean ec
GROUP BY 
    CASE 
        WHEN ec.Age BETWEEN 20 AND 29 THEN '20-29'
        WHEN ec.Age BETWEEN 30 AND 39 THEN '30-39'
        WHEN ec.Age BETWEEN 40 AND 49 THEN '40-49'
        ELSE '50+'
    END
ORDER BY attrition_rate DESC;
