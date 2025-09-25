#!/bin/bash
echo "🚀 Reloading and cleaning employee data..."

# Activate virtual environment
source venv/Scripts/activate

# Step 1: Load raw data into SQL Server
python scripts/load_data.py

# Step 2: Clean data, write to SQL, export fresh CSV for Tableau
python scripts/clean_data.py

echo "✅ Reload + Clean pipeline complete"
