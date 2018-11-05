from flask import jsonify, Response, request
from datetime import datetime
from . import app, db
from .models.task import Task
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


@app.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'GET':
        tasks = [task.serialize() for task in Task.query.all()]
        return jsonify(tasks)

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
