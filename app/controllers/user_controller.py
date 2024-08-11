from flask import Blueprint, jsonify
from app.services.user_service import get_users_service

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def health_check():
    checkAlive = 'I am alive!'
    return jsonify(checkAlive)

@user_bp.route('/api/users', methods=['GET'])
def get_users():
    users = get_users_service()
    return jsonify(users)
