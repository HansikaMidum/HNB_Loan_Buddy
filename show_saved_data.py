import sqlite3

DB_FILE = 'chat_training_data.db'

def show_saved_data():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, user_input, predicted_tag FROM training_data')
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        print("No training data saved yet.")
    else:
        print("Saved training data:")
        for row in rows:
            print(f"ID: {row[0]}, User Input: {row[1]}, Predicted Tag: {row[2]}")

if __name__ == '__main__':
    show_saved_data()
