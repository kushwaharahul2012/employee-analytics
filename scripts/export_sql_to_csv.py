import pandas as pd
from sqlalchemy import create_engine

# Connection string to SQL Server
conn_str = (
    "mssql+pyodbc://localhost/EmployeeAnalytics"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)
engine = create_engine(conn_str)

# Query the raw table
query = "SELECT * FROM employees_raw"
df = pd.read_sql(query, engine)

# Save to CSV (for Tableau Public)
output_file = "data/employees_raw_from_sql.csv"
df.to_csv(output_file, index=False)

print(f"✅ Exported {len(df)} rows to {output_file}")
