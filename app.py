from flask import Flask, render_template, request, jsonify
from chatbot import chatbot_response  # Importing the chatbot logic
from training_data import init_db, save_training_example  # ⬅️ import functions

app = Flask(__name__)
init_db()  # ⬅️ initialize database when app starts

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    if not message:
        return jsonify({'reply': "Please type a message."})  # Handle empty messages

    response, tag = chatbot_response(message)  # Get both the response and the predicted tag
    save_training_example(message, tag)  # Save the user message and predicted tag in the database
    
    return jsonify({'reply': response})  # Send response back to the frontend

if __name__ == '__main__':
    app.run(debug=True)
