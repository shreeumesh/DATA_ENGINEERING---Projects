import pandas as pd
"""
pandas is the core library used for data engineering tasks such as:
- Reading structured data (CSV, Excel, DB)
- Cleaning and transforming data
- Preparing analytics-ready datasets

In real-world healthcare ETL, pandas is often used in
batch pipelines before loading data into databases or warehouses.
"""


# ============================================================
# EXTRACT STEP
# ============================================================

# read_csv():
# Definition:
# Reads a CSV file and loads it into a DataFrame (table-like structure).
#
# Why we use it:
# Most healthcare source systems export data as flat files (CSV)
# on a daily or hourly basis.
#
# Real-time example:
# Hospitals export patient demographics and encounter data
# from EMR systems into CSV files for analytics pipelines.
patients = pd.read_csv(
    "ETL_Projects\\Patient_visit_ETL\\Data\\patient.csv"
)

encounters = pd.read_csv(
    "ETL_Projects\\Patient_visit_ETL\\Data\\encounter.csv"
)


# ============================================================
# TRANSFORM STEP
# ============================================================

# ----------------------------
# Data Quality Rule #1
# ----------------------------

# dropna(subset=["patient_id"])
#
# Definition:
# Removes rows ONLY where 'patient_id' is missing.
#
# Why subset is CRITICAL:
# By default, dropna() removes rows if ANY column has nulls.
# That would incorrectly drop valid healthcare records.
#
# Healthcare reasoning:
# - patient_id is a business-critical key
# - Without patient_id, an encounter cannot be linked to a patient
# - Other columns (facility, visit_type) can be missing and still be usable
#
# Real-world analogy:
# If a hospital visit has no patient identifier, it is unusable.
# But if facility name is missing, the visit is still valid.
encounters = encounters.dropna(subset=["patient_id"])


# ----------------------------
# Data Standardization
# ----------------------------

# to_datetime():
#
# Definition:
# Converts string values into datetime objects.
#
# errors="coerce":
# - Invalid or missing dates are converted to NaT (Not a Time)
# - Prevents pipeline failure due to bad source data
#
# Real-time example:
# DOB values often come missing or in wrong formats.
# A robust ETL pipeline should not fail because of that.
patients["dob"] = pd.to_datetime(
    patients["dob"],
    errors="coerce"
)

encounters["visit_date"] = pd.to_datetime(
    encounters["visit_date"]
)


# ----------------------------
# Joining Datasets
# ----------------------------

# merge():
#
# Definition:
# Combines two DataFrames similar to a SQL JOIN.
#
# on="patient_id":
# - patient_id is the common business key
#
# how="inner":
# - Keeps only records that exist in BOTH datasets
#
# Why INNER JOIN?
# - Encounters without patient records are not useful for analytics
# - Ensures referential integrity
#
# Real-time healthcare example:
# Patient demographics often come from a master system,
# encounters from a transactional system.
# Joining them creates a complete patient-visit view.
patient_visits = encounters.merge(
    patients,
    on="patient_id",
    how="inner"
)


# ----------------------------
# Row-Level Metric Creation
# ----------------------------

# visit_count = 1
#
# Why do this?
# - Each row represents ONE encounter
# - visit_count acts as a row-level fact
#
# Real-world usage:
# In data warehouses and BI tools,
# metrics are calculated as SUM(visit_count)
#
# This design:
# - Simplifies analytics
# - Aligns with fact table modeling
# - Works well with dashboards
patient_visits["visit_count"] = 1


# ============================================================
# LOAD STEP (to curated file)
# ============================================================

# to_csv():
#
# Definition:
# Writes the DataFrame to a CSV file.
#
# index=False:
# - Prevents pandas from writing row numbers
#
# Real-time example:
# Cleaned and curated datasets are often:
# - Loaded into databases
# - Stored in curated data zones
# - Used by downstream analytics teams
patient_visits.to_csv(
    "ETL_Projects\\Patient_visit_ETL\\Data\\patient_visit_cleaned.csv",
    index=False
)


# ============================================================
# VALIDATION & LOGGING
# ============================================================

# Printing output for validation
#
# Real-world data engineering practice:
# - Always validate row counts
# - Ensure transformations didn’t drop data unexpectedly
print("Post Transformation Data\n")
print("\t\tCleaned Patient Visit Records\n")
print(patient_visits)

print("\nCleaned Record Count:", len(patient_visits))
