from flask import Blueprint, request, jsonify
from app.application.users.service import UserService
from app.infrastructure.api.repositories.users import UserRepository
from app.application.users.dto import UserDto

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/users/<string:id>', methods=['GET'])
def get_one(id):
    try:
        service = UserService(UserRepository())
        user = service.get_one(id)

        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email
        }), 200
    except Exception as err:
        return jsonify({"message": err.message, "code": err.code}), 400

@user_controller.route('/users', methods=['POST'])
def create():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    try:
        service = UserService(UserRepository())
        user = service.create(UserDto(name=name, email=email))

        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email
        }), 201
    except Exception as err:
        return jsonify({"message": err.message, "code": err.code}), 400

@user_controller.route('/users/<string:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    try:
        service = UserService(UserRepository())
        user = service.update(UserDto(id=id, name=name, email=email))

        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email
        }), 200
    except Exception as err:
        return jsonify({"message": err.message, "code": err.code}), 400
