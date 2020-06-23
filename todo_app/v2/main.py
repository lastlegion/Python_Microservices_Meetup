import logging

from flask import abort, Flask, request, jsonify

from service.todo_service import TodoService
from repository.todo_repository import TodoRepository


app = Flask(__name__)

repository = TodoRepository(db='./todo.db')
service = TodoService(repository=repository)

@app.route('/todo', methods=['POST'])
def add_todo():
    '''Adding items to a list'''
    description, status = None, None
    try:
        todo_item = request.get_json()
        description, status = todo_item['description'], todo_item['status']
    except Exception as e:
        logging.info(f'Failed to parse request body {e}')
        abort(400)
    service.add_todo(description, status)
    return jsonify({})

@app.route('/todo', methods=['GET'])
def get_todos():
    '''Get all items from the list'''
    response = service.list_todo()
    return jsonify(response)

@app.route('/todo/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id: int):
    '''Get all items from the list'''
    description, status = None, None
    try:
        todo_item = request.get_json()
        description, status = todo_item['description'], todo_item['status']
    except Exception as e:
        logging.info(f'Failed to parse request body {e}')
        abort(400)
    response = service.update_todo(id_=todo_id,
                                   description=description,
                                   status=status)
    return jsonify(response)

@app.route('/todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id: int):
    '''Get all items from the list'''
    response = service.delete_todo(id_=todo_id)
    return jsonify(response)

