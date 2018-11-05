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
    new_task = Task(title=request.json['title'],
                    content=request.json['content'])
    db.session.add(new_task)
    db.session.commit()

    response = jsonify(new_task.serialize())
    response.headers['Location'] = f"/items/{new_task.task_id}"
    response.status_code = 201
    return response

@app.route('/items/<int:id>', methods=['GET','PUT', 'DELETE'])
def item(id):
    if request.method == 'GET':
        task = Task.query.get(id)
        if task:
            return jsonify(task.serialize())
        else:
            return Response(status=404)
    elif request.method == 'PUT':
        task = Task.query.get(id)
        if task:
            task.title = request.json['title']
            task.content = request.json['content']
            db.session.add(task)
            db.session.commit()
            return Response(status=200)
        else:
            return Response(status=400)
