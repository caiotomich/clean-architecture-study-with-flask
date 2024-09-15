from functools import wraps
from flask import request, jsonify
from app.application.auth.services.token import Token

def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            current_user = Token.decode(token)
        except Exception as e:
            return jsonify({'message': str(e)}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated
