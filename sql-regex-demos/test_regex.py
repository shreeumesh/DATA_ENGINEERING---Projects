"""
SQL Regex Demo - Healthcare Data
Uses Python re module regex (no SQL LIKE)
"""

import sqlite3
import re  # Python regex module

# Create database
conn = sqlite3.connect('patients.db')
c = conn.cursor()

# Create table
c.execute('''
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    diagnosis TEXT
)
''')

# Clear data
c.execute('DELETE FROM patients')

# Insert sample data
data = [
    ('John Doe', 'john.doe@email.com', '123-456-7890', 'Diabetes Type 2'),
    ('Jane Smith', 'jane.smith@email.com', '987-654-3210', 'Hypertension'),
    ('Mike Johnson', 'mike.j@email.com', '555-123-4567', 'Asthma'),
    ('Sarah Wilson', 'sarah.w@email.com', '444-777-8888', 'Diabetes'),
    ('Bob Lee', 'bob.lee@email.com', '111-222-3333', 'Hypertension')
]

c.executemany('INSERT INTO patients (name, email, phone, diagnosis) VALUES (?, ?, ?, ?)', data)
conn.commit()

print("Table created with 5 patient records")

# Show all data
print("\nSample data:")
for row in c.execute('SELECT * FROM patients'):
    print(f"ID:{row[0]} | {row[1]} | {row[2]} | {row[3]}")

# ========================================
# STRICTLY PYTHON REGEX - Email matching
# ========================================
print("\nEmail pattern test (regex '@.*email\\.com'):")
email_regex = r'@.*email\.com$'  # Matches @ followed by anything then email.com

matching_emails = []
for row in c.execute('SELECT name, email FROM patients'):
    if re.search(email_regex, row[1]):  # Pure Python regex
        matching_emails.append((row[0], row[1]))

for name, email in matching_emails:
    print(f"{name}: {email}")

print("\nDemo completed")
