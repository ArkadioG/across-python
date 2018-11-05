from backend import app
from flask import jsonify, Response, request
from .mock_items import mocked_tasks
from datetime import datetime

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


@app.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'GET':
        return jsonify(mocked_tasks)

    # POST
    new_task = {'title': request.json['title'],
                'content': request.json['content'],
                'createdOn': datetime.utcnow()}

    return jsonify(new_task)


@app.route('/items/<int:id>')
def item(id):
    for task in mocked_tasks:
        if task["id"] == id:
            return jsonify(task)
    else:
        return Response(status=404)
