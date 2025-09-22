# Employee Analytics Project (30-Day Challenge)

**Description**
This project builds an end-to-end Employee Analytics & Reporting System using Python, SQL, Tableau & Bash.  
Daily commits track progress through the 30-day challenge (repo: `employee-analytics`).

## Project Goal
Build a pipeline that cleans HR data, loads it into SQL, produces KPI queries, and visualizes insights in Tableau. Automate daily refresh via Bash.

## Tools / Tech
- Python (pandas, sqlalchemy, pytest)
- SQL (Postgres/SQLite/MySQL)
- Tableau (desktop / public)
- Bash (cron jobs, scripts)
- GitHub (repo, issues, actions)

## Folder structure
- `data/` — raw datasets (CSV)
- `scripts/` — Python ETL scripts & helpers
- `sql/` — schema DDL and queries
- `dashboards/` — Tableau screenshots / exports
- `docs/` — architecture, ERD, README extras
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

**How to use this repo**
1. Day-by-day tasks documented in GitHub Project (Kanban).  
2. Day 3 onwards: run `scripts/etl.py` to load and clean data (template scripts will be added).  
