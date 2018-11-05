from backend import app
from flask import jsonify
from .mock_items import mocked_tasks

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


@app.route('/items')
def items():
    return jsonify(mocked_tasks)
