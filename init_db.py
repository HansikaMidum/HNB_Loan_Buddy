import sqlite3

# Connect to the database (creates file if it doesn't exist)
conn = sqlite3.connect('training_data.db')
cursor = conn.cursor()

# Create training_data table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS training_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT NOT NULL,
        tag TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

conn.commit()
conn.close()
print("✅ SQLite database and table created successfully.")
