#!/bin/bash
set -euo pipefail

echo "=============================="
echo "🚀 Running Data Pipeline"
echo "=============================="

echo "[1/5] Step 1: Run data validation..."
python scripts/validate_data.py

# If validation_report.csv exists and has content, stop pipeline
if [ -s validation_report.csv ]; then
  echo "❌ Validation failed. See validation_report.csv"
  exit 1
else
  echo "✅ Validation passed. Continuing..."
fi

echo "[2/5] Step 2: Run data cleaning..."
python scripts/clean_data.py

echo "[3/5] Step 3: Load cleaned data into SQL..."
python scripts/load_clean_to_sql.py

echo "[4/5] Step 4: Normalize into relational tables..."
python scripts/normalize.py

echo "[5/5] Step 5: Export analysis view for Tableau..."
python scripts/export_tableau_csvs.py

echo "=============================="
echo "🎯 Pipeline completed successfully at $(date)"
echo "=============================="
