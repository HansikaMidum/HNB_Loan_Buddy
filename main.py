from flask import Flask, render_template, request, jsonify
from chatbot import chatbot_response

app = Flask(__name__)

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
    reply = chatbot_response(message)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
