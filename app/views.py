from flask import Blueprint
from .responses import response

app_v1 = Blueprint('api', __name__, url_prefix='/api/v1')


@app_v1.route('/tasks', methods=['GET'])
def get_tasks():
    return response({
        'message': 'Funciona'
    })


@app_v1.route('/tasks/<id>', methods=['GET'])
def get_task():
    pass


@app_v1.route('/tasks', methods=['POST'])
def create_task():
    pass


@app_v1.route('/tasks/<id>', methods=['PUT'])
def update_task():
    pass


@app_v1.route('/tasks/<id>', methods=['DELETE'])
def delete_task():
    pass
