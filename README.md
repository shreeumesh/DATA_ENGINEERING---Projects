# 💡 Healthcare Data ETL Pipeline

## 📖 Project Overview

This project is a **modular ETL pipeline** built in Python that simulates a real-world data engineering workflow:

🔹 Extracting raw healthcare/structured data  
🔹 Cleaning and transforming datasets  
🔹 Loading into a structured database  

This pipeline demonstrates the core principles of production-grade ETL architecture.

---

## ⚙️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-025E8C?style=for-the-badge&logo=postgresql&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)

---

## 🚀 Architecture

Raw Data → Extract → Transform → Validate → Load → Database

---

## 🔄 Pipeline Workflow

1. **Extract**
   - Loads raw CSV files from `data/`
2. **Transform**
   - Cleans missing values
   - Standardizes columns
   - Applies business rules
3. **Validate**
   - Checks schema & integrity rules
4. **Load**
   - Inserts processed data into PostgreSQL
   - Ensures integrity via optimized SQL

---

## 📂 Project Structure

