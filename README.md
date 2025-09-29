# Employee Analytics Project (30-Day Challenge)

**Description**  
This project builds an end-to-end Employee Analytics & Reporting System using Python, SQL, Tableau & Bash.  
Daily commits track progress through the 30-day challenge (repo: `employee-analytics`).  

## Project Goal  
Build a pipeline that cleans HR data, loads it into SQL, produces KPI queries, and visualizes insights in Tableau. Automate daily refresh via Bash.  

## Tools / Tech  
- Python (pandas, sqlalchemy, matplotlib, pytest)  
- SQL (SQL Server / Postgres / MySQL)  
- Tableau (desktop / public)  
- Bash (automation scripts)  
- GitHub (repo, issues, actions)  

## Folder structure  
- `data/` — raw datasets (CSV)  
- `scripts/` — Python ETL scripts & helpers  
- `sql/` — schema DDL and queries  
- `tableau/` — Tableau dashboards  
- `bash/` — automation shell scripts  
- `docs/` — ERD, design notes  
- `tests/` — unit tests (pytest)  

## Dataset Schema — `data/employee_data.csv`

| Column              | Description                                              | Example        |
|---------------------|----------------------------------------------------------|----------------|
| **EmployeeID**      | Unique identifier for each employee                      | 1001           |
| **Name**            | Employee name (synthetic / anonymized)                   | Employee_1001  |
| **Department**      | Department name                                          | IT, Finance    |
| **Gender**          | Gender (Male / Female / Other)                           | Male           |
| **Age**             | Employee age                                             | 32             |
| **Salary**          | Current annual salary (synthetic, numeric)               | 75000          |
| **JoinYear**        | Year employee joined                                     | 2018           |
| **Attrition**       | Whether employee left (`Yes` / `No`)                     | No             |
| **PerformanceRating** | Performance score (1 low → 5 high)                    | 4              |

## Daily Progress

### Day 1 — Setup & Repo Init  
- Create repo `employee-analytics`  
- Setup Python virtual environment & requirements  
- Add raw HR dataset to `/data`  

### Day 2 — SQL Schema Setup  
- Create `employees_raw` table  
- Import dataset into SQL Server (SSMS)  
- Validate row counts  

### Day 3 — Python ETL Script  
- Build first ETL (`scripts/etl.py`) to load CSV → SQL  
- Basic logging & error handling added  

### Day 4 — Data Cleaning Pipeline  
- Python cleaning script handles nulls, duplicates, inconsistent casing  
- Create new table `employees_clean`  
- Export cleaned CSV → Tableau-ready  
- Bash automation runs cleaning in one command  

### Day 5 — Data Normalization  
- Normalize into relational tables:  
  - `employees`  
  - `departments`  
  - `salaries`  
  - `performance`  
- Insert transformed data into normalized schema  

### Day 6 — Data Validation & Integrity  
- Add SQL `CHECK` constraints (salary > 0, KPI 1–5, valid join year)  
- Python validation script creates `validation_report.csv`  
- Tableau Data Quality Dashboard: Pass/Fail + Error Breakdown  
- Bash pipeline stops if validation fails  

### Day 7 — Exploratory Data Analysis (EDA)  
- SQL queries for avg salary by department, attrition rates, top performers  
- Python plots: salary distribution, KPI vs Salary correlation  
- Tableau dashboard: salary by dept, attrition by dept, scatter plot KPI vs Salary  

### Day 8 — Attrition Analysis  
- SQL: attrition % by department/gender/age group  
- Python logistic regression predicting attrition probability  
- Tableau: attrition trend dashboard  
- Bash pipeline step: export attrition summary  

### Day 9 — Salary vs KPI Deep Dive  
- SQL queries linking salaries & performance scores  
- Python: correlation heatmap, salary outlier detection  
- Tableau: KPI vs Salary dashboard with filters  
- Pipeline exports insights to `/analysis`  

### Day 10 — Departmental Performance Review  
- SQL: Avg KPI score by department  
- Python: departmental boxplots (KPI distribution)  
- Tableau: department comparison dashboard  

### Day 11 — Employee Tenure Analysis  
- SQL: Compute employee tenure = CurrentYear – JoinYear  
- Python: tenure distribution analysis  
- Tableau: attrition vs tenure visual  

### Day 12 — Gender Diversity Analysis  
- SQL: Male/Female/Other ratios per department  
- Python: bar chart & gender pay gap stats  
- Tableau: diversity dashboard  

### Day 13 — Age Demographics  
- SQL: Age buckets (20–29, 30–39, etc.)  
- Python: histogram & skewness analysis  
- Tableau: workforce age pyramid  

### Day 14 — Salary Forecasting Prep  
- SQL: Salary growth per department (trend by join year)  
- Python: time-series prep for forecasting salaries  
- Tableau: salary trends dashboard  

### Day 15 — Performance Prediction (ML Intro)  
- SQL: Extract features for ML (Age, Dept, Salary, Tenure)  
- Python: basic ML model (scikit-learn decision tree) to predict KPI category  
- Tableau: feature importance visualization  