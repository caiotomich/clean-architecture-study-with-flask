from flask import Blueprint, request, jsonify
from app.domain.entities.user.service import UserService

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()

@user_controller.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all()
    return jsonify([{
        'id': user.id,
        'name': user.name,
        'email': user.email
    } for user in users]), 200

@user_controller.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = user_service.get_user(id)
    if user:
        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email
        }), 200
    else:
        return jsonify({'message': 'User not found'}), 404

@user_controller.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    if not name or not email:
        return jsonify({'message': 'Name and email are required'}), 400
    
    try:
        user = user_service.create_user(name, email)

        print('user:', user)
    except Exception as err:
        return jsonify({'message': 'User already exists', 'error': str(err)}), 400

    return jsonify({
        'id': user.id,
        'name': user.name,
        'email': user.email
    }), 201

@user_controller.route('/users/<string:user_uuid>', methods=['DELETE'])
def delete_user(user_uuid):
    user = user_service.delete_user(user_uuid)
    if user:
        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email
        }), 200
    else:
        return jsonify({'message': 'User not found'}), 404
