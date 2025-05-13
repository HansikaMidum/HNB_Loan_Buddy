# training_data.py
import sqlite3

DB_FILE = 'chat_training_data.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS training_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT NOT NULL,
            predicted_tag TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

import re

def save_training_example(user_input, predicted_tag):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO training_data (user_input, predicted_tag) VALUES (?, ?)', (user_input, predicted_tag))
    conn.commit()
    conn.close()
    print(f"✅ Training example saved: {user_input} -> {predicted_tag}")

def categorize_message(message):
    # Check if message is symbol category (contains only symbols, digits, or single letters)
    if re.fullmatch(r'[\W\d_]+', message) or re.fullmatch(r'[a-zA-Z]', message):
        return 'symbol'
    # Check if message is information category (common info questions)
    info_patterns = [
        r'how are you',
        r'what is your name',
        r'where are you from',
        r'who are you',
        r'what do you do',
        r'how old are you'
    ]
    for pattern in info_patterns:
        if re.search(pattern, message, re.IGNORECASE):
            return 'information'
    # Otherwise, categorize as other
    return 'other'

def save_categorized_training_example(user_input):
    tag = categorize_message(user_input)
    save_training_example(user_input, tag)
