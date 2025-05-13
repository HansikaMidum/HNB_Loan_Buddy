import sqlite3
import string
import nltk
import numpy as np
import pickle
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('punkt')
nltk.download('wordnet')

DB_FILE = 'chat_training_data.db'

def train_model_from_db():
    # Initialize tools
    lemmatizer = WordNetLemmatizer()

    # Connect to DB and fetch data
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT user_input, predicted_tag FROM training_data')
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No training data found in the database.")
        return

    corpus = []
    labels = []

    for user_input, predicted_tag in rows:
        tokens = nltk.word_tokenize(user_input)
        tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens if word not in string.punctuation]
        corpus.append(' '.join(tokens))
        labels.append(predicted_tag)

    # Vectorization
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus).toarray()

    # Encode labels
    unique_labels = list(set(labels))
    label_mapping = {label: idx for idx, label in enumerate(unique_labels)}
    y = np.array([label_mapping[label] for label in labels])

    # Train model
    model = LogisticRegression()
    model.fit(X, y)

    print(f"✅ Model Trained and Saved on DB data!")

    # Save model and vectorizer
    pickle.dump(model, open('model.pkl', 'wb'))
    pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
    pickle.dump(label_mapping, open('label_mapping.pkl', 'wb'))

if __name__ == "__main__":
    train_model_from_db()
