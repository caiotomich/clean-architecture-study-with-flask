from flask import Blueprint, request, jsonify

api_controller = Blueprint('api_controller', __name__)

@api_controller.route('/', methods=['GET'])
def root():
    return jsonify({'success': True, 'message': 'Everything is running fine.'}), 200