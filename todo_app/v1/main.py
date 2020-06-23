import sqlite3
import logging
from flask import abort, Flask, request, jsonify

app = Flask(__name__)

@app.route('/todo', methods=['POST'])
def add_todo():
    '''Adding items to a list'''
    item, status = None, None
    try:
        todo_item = request.get_json()
        item, status = todo_item['item'], todo_item['status']
    except Exception as e:
        logging.info(f'Failed to parse request body {e}')
        abort(400)



    return jsonify({})

@app.route('/todo', methods=['GET'])
def get_todos():
    '''Get all items from the list'''
    return jsonify({})

@app.route('/todo/<:id>', method=['UPDATE'])
def update_todos():
    return jsonify({})

@app.route('/todo/<:id>', method=['DELETE'])
def delete_todos():
    return jsonify({})