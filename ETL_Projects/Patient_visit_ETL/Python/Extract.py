import pandas as pd

# pandas: Python library used for data manipulation and analysis
# Real-time use: Almost every ETL pipeline uses pandas to read, clean,
# transform, and prepare structured data like CSV, Excel, or database tables.


# =========================
# EXTRACT STEP
# =========================

# read_csv():
# Definition: Reads data from a CSV file and loads it into a DataFrame (table-like structure).
# Real-time example:
# In healthcare, patient and encounter data often arrives as daily CSV files
# from hospital systems or vendors.

patients = pd.read_csv("ETL_Projects\Patient_visit_ETL\Data\encounter.csv")
encounter = pd.read_csv("ETL_Projects\Patient_visit_ETL\Data\patient.csv")

print("\t\t Patients Data: ")
print(patients)

print("\n\t\t Encounter Data: ")
print(encounter)

print("\nPatient count : ",len(patients))
print("\nEncounter Count : ",len(encounter))

