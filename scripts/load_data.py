#!/usr/bin/env python3
"""
Load employee CSV and persist to SQL Server table `employees_raw`.

Configuration (via environment variables or .env):
  - SQL_SERVER      (default: localhost)
  - SQL_DATABASE    (default: EmployeeAnalytics)
  - SQL_USERNAME    (optional; required if not using trusted connection)
  - SQL_PASSWORD    (optional; required if not using trusted connection)
  - SQL_DRIVER      (default: "ODBC Driver 17 for SQL Server")
  - SQL_TRUSTED     (yes/no) default: yes (use Windows Integrated auth)

Example .env:
  SQL_SERVER=localhost
  SQL_DATABASE=EmployeeAnalytics
  SQL_TRUSTED=yes
  # or for SQL auth:
  # SQL_TRUSTED=no
  # SQL_USERNAME=sa
  # SQL_PASSWORD=yourStrong(!)Password
"""

import os
import logging
import sys
from pathlib import Path
import urllib.parse

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load .env if present
load_dotenv()

# Logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Config (defaults)
SQL_SERVER = os.getenv("SQL_SERVER", "localhost")
SQL_DATABASE = os.getenv("SQL_DATABASE", "EmployeeAnalytics")
SQL_USERNAME = os.getenv("SQL_USERNAME", "")
SQL_PASSWORD = os.getenv("SQL_PASSWORD", "")
SQL_DRIVER = os.getenv("SQL_DRIVER", "ODBC Driver 17 for SQL Server")
SQL_TRUSTED = os.getenv("SQL_TRUSTED", "yes").lower()  # 'yes' or 'no'

INPUT_CSV = Path("data/employee_data.csv")
TABLE_NAME = "employees_raw"

def build_engine_url():
    """
    Build a SQLAlchemy engine URL for SQL Server via pyodbc.
    Uses the odbc_connect parameter (URL-encoded).
    """
    if SQL_TRUSTED in ("1", "true", "yes", "y"):
        odbc_str = (
            f"DRIVER={{{SQL_DRIVER}}};"
            f"SERVER={SQL_SERVER};"
            f"DATABASE={SQL_DATABASE};"
            f"Trusted_Connection=yes;"
        )
    else:
        if not SQL_USERNAME or not SQL_PASSWORD:
            logging.error("SQL_AUTH selected but SQL_USERNAME/SQL_PASSWORD not provided.")
            raise SystemExit("Provide SQL_USERNAME and SQL_PASSWORD in environment or .env or set SQL_TRUSTED=yes")
        odbc_str = (
            f"DRIVER={{{SQL_DRIVER}}};"
            f"SERVER={SQL_SERVER};"
            f"DATABASE={SQL_DATABASE};"
            f"UID={SQL_USERNAME};PWD={SQL_PASSWORD};"
        )

    quoted = urllib.parse.quote_plus(odbc_str)
    engine_url = f"mssql+pyodbc:///?odbc_connect={quoted}"
    return engine_url

def main():
    # Check input
    if not INPUT_CSV.exists():
        logging.error(f"Input CSV not found: {INPUT_CSV.resolve()}")
        sys.exit(1)

    # Load CSV
    logging.info(f"Loading CSV: {INPUT_CSV}")
    df = pd.read_csv(INPUT_CSV)
    logging.info(f"Loaded data shape: {df.shape}")
    logging.info(f"Columns: {df.columns.tolist()}")
    logging.info("Sample rows:\n%s", df.head().to_string())

    # Build engine and persist to SQL Server
    try:
        engine_url = build_engine_url()
        logging.info("Creating SQLAlchemy engine.")
        engine = create_engine(engine_url, echo=False)
    except Exception as e:
        logging.exception("Failed building SQLAlchemy engine. Check driver and connection params.")
        raise SystemExit(e)

    try:
        logging.info("Writing DataFrame to SQL Server table: %s", TABLE_NAME)
        # For modest datasets (500 rows) default to_sql is OK.
        df.to_sql(TABLE_NAME, con=engine, if_exists="replace", index=False)
        logging.info("✅ Data written to SQL Server (table: %s) in database %s@%s", TABLE_NAME, SQL_DATABASE, SQL_SERVER)
    except Exception as e:
        logging.exception("Failed writing DataFrame to SQL Server. Common issues: ODBC driver not installed, wrong auth, or network.")
        raise SystemExit(e)
    finally:
        try:
            engine.dispose()
        except Exception:
            pass

if __name__ == "__main__":
    main()
