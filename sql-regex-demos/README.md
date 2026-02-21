# SQL Regex Demo

SQLite database with healthcare sample data for testing SQL REGEXP patterns and data cleaning techniques.

## Quick Start

```bash
python test_regex.py


OUTPUT:
Table created with 5 patient records

Sample data:
ID:1 | John Doe | john.doe@email.com | 123-456-7890 | Diabetes Type 2
ID:2 | Jane Smith | jane.smith@email.com | 987-654-3210 | Hypertension
ID:3 | Mike Johnson | mike.j@email.com | 555-123-4567 | Asthma
ID:4 | Sarah Wilson | sarah.w@email.com | 444-777-8888 | Diabetes
ID:5 | Bob Lee | bob.lee@email.com | 111-222-3333 | Hypertension

Email pattern test (LIKE '%@email.com'):
John Doe: john.doe@email.com
Jane Smith: jane.smith@email.com
Sarah Wilson: sarah.w@email.com
Bob Lee: bob.lee@email.com

Demo completed
