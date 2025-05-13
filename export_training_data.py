import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('training_data.db')
cursor = conn.cursor()

# Create a directory if not exists (optional for larger projects)
import os
os.makedirs("exports", exist_ok=True)

# Export to CSV
with open('exports/training_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['message', 'tag'])  # Header

    for row in cursor.execute("SELECT message, tag FROM training_data"):
        writer.writerow(row)

conn.close()
print("✅ Training data exported successfully to 'exports/training_data.csv'")
