from flask import Blueprint, request
from .responses import response, not_found
from .models.task import Task

app_v1 = Blueprint('api', __name__, url_prefix='/api/v1')


@app_v1.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return response([task.serialize() for task in tasks])


@app_v1.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    task = Task.query.filter_by(id=id).first()

    if task is None:
        return not_found()

    return response(task.serialize())


@app_v1.route('/tasks', methods=['POST'])
def create_task():
    json = request.get_json(force=True)
    task = Task.new(json['title'], json['description'], json['deadline'])
    if task.save():
        return response(task.serialize())

    return {}


@app_v1.route('/tasks/<id>', methods=['PUT'])
def update_task():
    pass


@app_v1.route('/tasks/<id>', methods=['DELETE'])
def delete_task():
    pass
