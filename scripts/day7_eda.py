import pandas as pd
import matplotlib.pyplot as plt
import pyodbc
import os

# ============================
# Day 7 EDA - Employee Analytics
# ============================

# Ensure output folder exists
os.makedirs("analysis", exist_ok=True)

# Connect to SQL Server
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-498K8OT;"
    "Database=EmployeeAnalytics;"
    "Trusted_Connection=yes;"
)

# Query: Join employees, departments, salaries, performance, attrition
query = """
SELECT e.employee_id, e.first_name, e.last_name,
       d.department_name, s.salary, p.kpi_score,
       ec.Age, ec.Attrition
FROM dbo.employees e
JOIN dbo.departments d ON e.department_id = d.department_id
JOIN dbo.salaries s ON e.employee_id = s.employee_id
JOIN dbo.performance p ON e.employee_id = p.employee_id
JOIN dbo.employees_clean ec ON e.employee_id = ec.EmployeeID;
"""

df = pd.read_sql(query, conn)

# ----------------------------
# Plot 1: Salary Distribution
# ----------------------------
plt.figure(figsize=(8,6))
df["salary"].hist(bins=20)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Count")
plt.savefig("analysis/day7_salary_distribution.png")
plt.close()

# ----------------------------
# Plot 2: KPI vs Salary Scatter
# ----------------------------
plt.figure(figsize=(8,6))
df.plot.scatter(x="kpi_score", y="salary", alpha=0.6)
plt.title("KPI Score vs Salary")
plt.xlabel("KPI Score")
plt.ylabel("Salary")
plt.savefig("analysis/day7_kpi_vs_salary.png")
plt.close()

# ----------------------------
# Plot 3: Attrition vs Age
# ----------------------------
plt.figure(figsize=(8,6))
attrition_age = df.groupby(["Age", "Attrition"]).size().unstack(fill_value=0)
attrition_age.plot(kind="bar", stacked=True, figsize=(10,6))
plt.title("Attrition vs Age")
plt.xlabel("Age")
plt.ylabel("Count")
plt.legend(title="Attrition")
plt.tight_layout()
plt.savefig("analysis/day7_attrition_vs_age.png")
plt.close()

# ----------------------------
# Export CSV for Tableau Public
# ----------------------------
csv_path = "analysis/day7_eda.csv"
df.to_csv(csv_path, index=False)
print(f"✅ EDA Plots + CSV generated. Tableau dataset saved to {csv_path}")
