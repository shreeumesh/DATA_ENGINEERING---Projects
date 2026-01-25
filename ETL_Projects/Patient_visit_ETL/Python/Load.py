import pandas as pd
import sqlite3

# ----------------------------
# Read cleaned data
# ----------------------------

# This is the output of the Transform step
patient_visits = pd.read_csv(
    "ETL_Projects\\Patient_visit_ETL\\Data\\patient_visit_cleaned.csv"
)

# ----------------------------
# Connect to SQLite database
# ----------------------------

# This creates healthcare.db if it does not exist
conn = sqlite3.connect(
    "ETL_Projects\\Patient_visit_ETL\\Python\\healthcare.db"
)

# ----------------------------
# Load data into SQL table
# ----------------------------

# to_sql():
# - table name: patient_visits
# - if_exists="replace" → overwrite table (safe for learning)
# - index=False → do not store pandas index
patient_visits.to_sql(
    "patient_visits",
    conn,
    if_exists="replace",
    index=False
)

# ----------------------------
# Close connection
# ----------------------------

conn.close()

print("Load step completed: Data loaded into healthcare.db")