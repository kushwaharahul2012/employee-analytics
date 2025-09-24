import pandas as pd

# Load dataset
df = pd.read_csv("data/employee_data.csv")

# Show basic info
print("Shape of dataset:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())

# Quick summary
print("\nData Types:\n", df.dtypes)
print("\nNull values:\n", df.isnull().sum())