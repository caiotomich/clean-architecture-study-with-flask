from flask import Blueprint, request, jsonify, make_response
from app.infra.api.middlewares.auth_decorator import protected
from app.application.auth.services.token import Token
from app.application.users.services.authenticate import UserAuthenticateService

authentication = Blueprint('authentication', __name__)

@authentication.route('/login', methods=['GET'])
def login():
    auth = request.authorization

    if not auth or not auth.email or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    user = UserAuthenticateService.authenticate(auth.email, auth.password)
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    token = Token.generate(user)
    return jsonify({'token': token})

@authentication.route('/authcheck', methods=['GET'])
@protected
def authcheck(user):
    return jsonify({'success': True, 'user': user}), 200
