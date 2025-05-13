import random
import json
import pickle
import nltk
import string
import numpy as np
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

# Load files
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
label_mapping = pickle.load(open('label_mapping.pkl', 'rb'))
reverse_label_mapping = {v: k for k, v in label_mapping.items()}

lemmatizer = WordNetLemmatizer()

with open('intents.json', 'r') as file:
    intents = json.load(file)

def clean_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens if word not in string.punctuation]
    return ' '.join(tokens)

def predict_class(text):
    clean = clean_text(text)
    X = vectorizer.transform([clean]).toarray()
    prediction = model.predict(X)[0]
    tag = reverse_label_mapping[prediction]  # ✅ correct tag from index
    return tag

def get_response(tag):
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

def chatbot_response(text):
    tag = predict_class(text)
    response = get_response(tag)
    return response

# chatbot.py
# ... (imports and existing code)

def chatbot_response(text):
    tag = predict_class(text)
    response = get_response(tag)
    return response, tag  # return both response and tag

