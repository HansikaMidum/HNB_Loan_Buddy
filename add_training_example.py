import sqlite3

DB_FILE = 'chat_training_data.db'

def add_training_example(user_input, tag):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO training_data (user_input, predicted_tag) VALUES (?, ?)', (user_input, tag))
    conn.commit()
    conn.close()
    print(f"✅ Training example added: {user_input} -> {tag}")

if __name__ == '__main__':
    print("Add new training examples to the chatbot database.")
    while True:
        user_input = input("Enter user input (or 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            break
        tag = input("Enter category/tag for this input: ").strip()
        if not tag:
            print("Tag cannot be empty. Try again.")
            continue
        add_training_example(user_input, tag)
