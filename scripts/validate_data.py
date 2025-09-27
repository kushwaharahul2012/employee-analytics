# Day 6: Data Validation Script
# This script validates employees_clean data and produces a validation_report.csv

import os
import pandas as pd
from sqlalchemy import create_engine

# Connection string - replace with your actual credentials or environment variable
DB_URL = os.getenv("EMP_DB_URL", "mssql+pyodbc://@DESKTOP-498K8OT/employeeanalytics?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes")

# Create connection
engine = create_engine(DB_URL)

# Load cleaned table
df = pd.read_sql("SELECT * FROM dbo.employees_clean", engine)

# TEMP TEST: force some invalid rows to simulate errors
df.loc[len(df)] = [9999, "FakeUser", "IT", "Male", 30, -5000, 2026, "No", 7]  # invalid salary + year + rating


# Validation checks
issues = []

# Salary must be positive
invalid_salary = df[df['Salary'] <= 0]
if not invalid_salary.empty:
    invalid_salary = invalid_salary.copy()
    invalid_salary.loc[:, 'error'] = "Invalid Salary"
    issues.append(invalid_salary)

# JoinYear must be between 2000 and current year
invalid_year = df[(df['JoinYear'] < 2000) | (df['JoinYear'] > 2025)]
if not invalid_year.empty:
    invalid_year = invalid_year.copy()
    invalid_year.loc[:, 'error'] = "Invalid JoinYear"
    issues.append(invalid_year)

# PerformanceRating must be between 1 and 5
invalid_perf = df[(df['PerformanceRating'] < 1) | (df['PerformanceRating'] > 5)]
if not invalid_perf.empty:
    invalid_perf = invalid_perf.copy()
    invalid_perf.loc[:, 'error'] = "Invalid PerformanceRating"
    issues.append(invalid_perf)

# Department must not be null
invalid_dept = df[df['Department'].isnull()]
if not invalid_dept.empty:
    invalid_dept =invalid_dept.copy()
    invalid_dept.loc[:,'error'] = "Missing Department"
    issues.append(invalid_dept)

# Combine and export
if issues:
    validation_report = pd.concat(issues)
    validation_report.to_csv("validation_report.csv", index=False)
    print(f"❌ Validation failed. Found {len(validation_report)} invalid rows. See validation_report.csv")
else:
    print("✅ Validation passed. No issues found.")
