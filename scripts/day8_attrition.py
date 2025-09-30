import pandas as pd
import pyodbc
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# ============================
# Day 8 Attrition Analysis
# Logistic Regression Model
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

# Pull data
query = """
SELECT ec.EmployeeID, ec.Age, ec.Gender, ec.Attrition,
       s.salary, p.kpi_score, d.department_name
FROM dbo.employees_clean ec
JOIN dbo.employees e ON ec.EmployeeID = e.employee_id
JOIN dbo.salaries s ON e.employee_id = s.employee_id
JOIN dbo.performance p ON e.employee_id = p.employee_id
JOIN dbo.departments d ON e.department_id = d.department_id;
"""
df = pd.read_sql(query, conn)

# Prepare features & labels
X = df[["Age", "Gender", "salary", "kpi_score", "department_name"]]
y = df["Attrition"].apply(lambda x: 1 if x == "Yes" else 0)

# One-hot encode categorical vars (Gender, Department)
categorical = ["Gender", "department_name"]
numeric = ["Age", "salary", "kpi_score"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(drop="first"), categorical),
        ("num", "passthrough", numeric)
    ]
)

# Build pipeline with preprocessing + logistic regression
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=500))
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
report = classification_report(y_test, y_pred, target_names=["Stay", "Attrition"])
print("Classification Report:\n", report)

# Predict probability of attrition for all employees
df["Attrition_Prob"] = model.predict_proba(X)[:, 1]

# Save to CSV for Tableau Public
csv_path = "analysis/day8_attrition.csv"
df.to_csv(csv_path, index=False)
print(f"✅ Logistic regression complete. Predictions saved to {csv_path}")
