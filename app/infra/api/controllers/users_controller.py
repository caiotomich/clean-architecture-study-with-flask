from flask import Blueprint, request, jsonify
from app.infra.api.repositories.users import UserRepository
from app.application.users.dto.create_dto import UserCreateDto
from app.application.users.dto.update_dto import UserUpdateDto
from app.application.users.dto.get_dto import UserGetDto
from app.application.users.services.get_one import UserGetOne
from app.application.users.services.get_all import UserGetAll
from app.application.users.services.create import UserCreate
from app.application.users.services.update import UserUpdate
from app.application.users.services.delete import UserDelete

users_controller = Blueprint('users_controller', __name__)

@users_controller.route('/users/<string:id>', methods=['GET'])
def get_one(id):
    try:
        user = UserGetOne(UserRepository()).execute(id=id)
        return jsonify(UserGetDto(user).data()), 200
    except Exception as err:
        message = err.message if err.message else 'Error on create user'
        code = err.code if err.code else 'UNEXPECTED_ERROR'
        return jsonify({"message": message, "code": code}), 400

@users_controller.route('/users', methods=['POST'])
def create():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    try:
        user_create = UserCreate(UserRepository())
        user = user_create.execute(UserCreateDto(name=name, email=email, password=password))

        return jsonify(UserGetDto(user).data()), 201
    except Exception as err:
        message = err.message if err.message else 'Error on create user'
        code = err.code if err.code else 'UNEXPECTED_ERROR'
        return jsonify({"message": message, "code": code}), 400

@users_controller.route('/users', methods=['GET'])
def get_all():
    try:
        users = UserGetAll(UserRepository()).execute()

        return jsonify([UserGetDto(user).data() for user in users]), 200
    except Exception as err:
        message = err.message if err.message else 'Error on create user'
        code = err.code if err.code else 'UNEXPECTED_ERROR'
        return jsonify({"message": message, "code": code}), 400


@users_controller.route('/users/<string:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    try:
        user_dto = UserUpdateDto(id=id, name=name, email=email)
        user_updated = UserUpdate(UserRepository()).execute(user_dto)
        user = UserGetDto(user_updated).data()

        return jsonify(user), 200
    except Exception as err:
        message = err.message if err.message else 'Error on create user'
        code = err.code if err.code else 'UNEXPECTED_ERROR'
        return jsonify({"message": message, "code": code}), 400

@users_controller.route('/users/<string:id>', methods=['DELETE'])
def delete(id):
    try:
        UserDelete(UserRepository()).execute(id)
        return jsonify({}), 200
    except Exception as err:
        message = err.message if err.message else 'Error on create user'
        code = err.code if err.code else 'UNEXPECTED_ERROR'
        return jsonify({"message": message, "code": code}), 400