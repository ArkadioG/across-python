from backend import app
from flask import jsonify, Response
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


@app.route('/items/<int:id>')
def item(id):
    for task in mocked_tasks:
        if task["id"] == id:
            return jsonify(task)
    else:
        return Response(status=404)
