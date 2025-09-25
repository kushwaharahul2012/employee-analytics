import pandas as pd
from sqlalchemy import create_engine

# Config
INPUT_CSV = "data/employee_data.csv"
CLEAN_TABLE = "employees_clean"
EXPORT_CSV = "data/employees_clean_from_sql.csv"

# SQL Server connection
conn_str = (
    "mssql+pyodbc://localhost/EmployeeAnalytics"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)
engine = create_engine(conn_str)

# Load CSV
df = pd.read_csv(INPUT_CSV)

# --- Cleaning steps ---
# Strip whitespace
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Ensure numeric types
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
df["PerformanceRating"] = pd.to_numeric(df["PerformanceRating"], errors="coerce")

# Fill missing values
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Salary"].fillna(df["Salary"].median(), inplace=True)
df["PerformanceRating"].fillna(df["PerformanceRating"].mode()[0], inplace=True)

# Normalize Attrition
df["Attrition"] = df["Attrition"].str.capitalize()
df["Attrition"] = df["Attrition"].where(df["Attrition"].isin(["Yes", "No"]), "No")

# Drop duplicates
df = df.drop_duplicates(subset=["EmployeeID"])

# --- Save cleaned data ---
df.to_sql(CLEAN_TABLE, engine, if_exists="replace", index=False)
print(f"✅ Cleaned data written to SQL table: {CLEAN_TABLE}")

# Export for Tableau
df.to_csv(EXPORT_CSV, index=False)
print(f"✅ Cleaned CSV exported for Tableau: {EXPORT_CSV}")

engine.dispose()
