import json
import string
import time  # ⏱️ Added for measuring training time
import nltk
import numpy as np
import pickle
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('punkt')
nltk.download('wordnet')

def train_model():
    # Initialize tools
    lemmatizer = WordNetLemmatizer()

    # Load intents
    with open('intents.json', 'r') as file:
        data = json.load(file)

    # Prepare data
    corpus = []
    labels = []

    for intent in data['intents']:
        for pattern in intent['patterns']:
            tokens = nltk.word_tokenize(pattern) # Tokenization 
            # Lemmatization & punctuation removal
            tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens if word not in string.punctuation] 
            corpus.append(' '.join(tokens))
            labels.append(intent['tag'])

    # Vectorization
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus).toarray()

    # Encode labels
    unique_labels = list(set(labels))
    label_mapping = {label: idx for idx, label in enumerate(unique_labels)}
    y = np.array([label_mapping[label] for label in labels])

    # ⏱️ Measure training time
    start = time.time()

    # Train model
    model = LogisticRegression()
    model.fit(X, y)

    end = time.time()
    print(f"✅ Model Trained and Saved! Training took {end - start:.2f} seconds.")

    # Save model and vectorizer
    pickle.dump(model, open('model.pkl', 'wb'))
    pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
    # Save label mapping too
    pickle.dump(label_mapping, open('label_mapping.pkl', 'wb'))

if __name__ == "__main__":
    train_model()





