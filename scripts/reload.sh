#!/bin/bash
echo "🚀 Reloading employees_raw from CSV into SQL Server..."

# Activate venv (adjust path if needed)
source venv/Scripts/activate

# Run the loader script
python scripts/load_data.py

# Export SQL table back to CSV for Tableau
python scripts/export_sql_to_csv.py

echo "✅ Reload complete"
