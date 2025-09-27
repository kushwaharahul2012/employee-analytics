# PSTB Project Log (Python + SQL + Tableau + Bash)

This file tracks the 30-day PSTB Challenge in an integrated, advanced format.  
Each day touches all 4 stacks (Python, SQL, Tableau, Bash).

---

## Day 1/30 – Project Setup & Raw Data Load

### ✅ Python
- Wrote ingestion script to read raw HR CSV.

### ✅ SQL
- Created database `employeeanalytics`.
- Created table `[dbo].[employees_raw]`.
- Loaded raw CSV data into `employees_raw`.

### ✅ Tableau
- Connected Tableau to the database (test connection only).

### ✅ Bash
- Added `ingest.sh` to automate raw data load into SQL.

🎯 Why this matters: Establishes the raw → DB → viz pipeline foundation.

---

## Day 2/30 – SQL Exploration & Basic Queries

### ✅ Python
- Verified ingestion script, exported sample data for quick inspection.

### ✅ SQL
- Ran basic queries on `employees_raw`: filtering, grouping, counts.
- Identified missing values and duplicate records.

### ✅ Tableau
- First draft viz (simple employee headcount by department).

### ✅ Bash
- Updated `ingest.sh` with logs.

🎯 Why this matters: Early insight into data issues before cleaning.

---

## Day 3/30 – Data Cleaning Prep

### ✅ Python
- Draft cleaning logic (remove nulls, handle duplicates, fix types).
- Created reusable cleaning functions.

### ✅ SQL
- Created test table for cleaned inserts.

### ✅ Tableau
- Verified which columns are needed for dashboards.

### ✅ Bash
- Added cleaning step stub into pipeline.

🎯 Why this matters: Prepares the ETL logic before building a stable clean dataset.

---

## Day 4/30 – Data Wrangling Day 🧹📊

### ✅ Python
- Completed cleaning script.
- Handled nulls, standardized formats, dropped duplicates.
- Output: clean DataFrame ready for SQL.

### ✅ SQL
- Created `[dbo].[employees_clean]`.
- Loaded cleaned data into `employees_clean`.

### ✅ Tableau
- Exported clean CSV for Tableau Public.
- Built distribution chart (employees by department).

### ✅ Bash
- Pipeline (`pipeline.sh`) now runs: raw → clean → SQL load → CSV export.

🎯 Why this matters: Clean data = reliable dashboards. Full pipeline automated.

---

## Day 5/30 – Normalize employees/salaries/performance tables

### ✅ Python
- Extended cleaning script to split data into employees, salaries, performance DataFrames.
- Prepared departments lookup DataFrame.

### ✅ SQL
- Created normalized tables: `employees`, `salaries`, `performance`, `departments` inside `employeeanalytics`.
- Populated them automatically from Python (INSERT via pyodbc/SQLAlchemy).

### ✅ Tableau
- Connected Tableau to normalized schema.
- Tested quick viz: salary vs KPI by department (JOIN across tables).

### ✅ Bash
- Updated pipeline: after cleaning, normalization step runs automatically.
- One command now loads both `employees_clean` and normalized tables.

🎯 Why this matters: Moves from flat data to relational design. Enables deeper analysis and richer Tableau dashboards.

---
