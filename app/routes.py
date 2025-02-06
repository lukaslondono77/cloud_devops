from flask import Blueprint, jsonify

routes = Blueprint('routes', __name__)

@routes.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify([])  # Returning an empty list as a placeholder
