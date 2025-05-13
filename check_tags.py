import sqlite3

DB_FILE = 'chat_training_data.db'

def check_tags():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT predicted_tag, COUNT(*) FROM training_data GROUP BY predicted_tag')
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No training data found.")
    else:
        print("Distinct predicted tags and their counts:")
        for tag, count in rows:
            print(f"Tag: {tag}, Count: {count}")

if __name__ == '__main__':
    check_tags()
