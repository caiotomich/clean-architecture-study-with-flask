from flask import Blueprint, request, jsonify
from app.infra.api.repositories.users import UserRepository
from app.application.users.dto.create_dto import UserCreateDto
from app.application.users.services.get_one import UserGetOne
from app.application.users.services.create import UserCreate
from app.application.users.services.update import UserUpdate
from app.application.users.services.delete import UserDelete

users_controller = Blueprint('users_controller', __name__)

@users_controller.route('/users/<string:id>', methods=['GET'])
def get_one(id):
    try:
        user = UserGetOne(UserRepository()).execute(id)

        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email
        }), 200
    except Exception as err:
        return jsonify({"message": err.message, "code": err.code}), 400

@users_controller.route('/users', methods=['POST'])
def create():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    try:
        user_dto = UserCreateDto(name=name, email=email, password=password)
        user = UserCreate(UserRepository()).execute(user_dto)

        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email
        }), 201
    except Exception as err:
        return jsonify({"message": err.message, "code": err.code}), 400

@users_controller.route('/users/<string:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    try:
        user_dto = UserCreateDto(id=id, name=name, email=email)
        user = UserUpdate(UserRepository()).execute(user_dto)

        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email
        }), 200
    except Exception as err:
        return jsonify({"message": err.message, "code": err.code}), 400

@users_controller.route('/users/<string:id>', methods=['DELETE'])
def delete(id):
    try:
        UserDelete(UserRepository()).execute(id)
        return jsonify({}), 200
    except Exception as err:
        if err.code == 'USER_NOT_FOUND':
            return jsonify({"message": err.message, "code": err.code}), 404
        return jsonify({"message": err.message, "code": err.code}), 400