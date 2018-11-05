from backend import app
from flask import jsonify



@app.route('/')
def home():
    return 'Hello across-stack!'


@app.route('/contact')
def contact():
    author_data = {
        "author": "Arek Gutkowski",
        "email": "me@example.com",
        "webpage": "example.com",
        "twitterName": "ArkadioG"
    }

    return jsonify(author_data)
