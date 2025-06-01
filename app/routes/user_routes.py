from flask import Flask, jsonify, request, Blueprint
from app.services.user_services import create_user, get_user, update_user, delete_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route("/", methods=["POST"])
def add_user():
    data = request.get_json()
    user_id = create_user(data)
    if user_id:
        return jsonify({"message": "User Created", "user_id":user_id}), 201
    else:
        return jsonify({"error":"Failed to create user"}), 400

@user_bp.route("/<int:user_id>", methods=["GET"])
def read_user(user_id):
    user = get_user(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User Not Found"}), 404                                  

@user_bp.route("/<int:user_id>", methods=["PUT"])
def alter_user(user_id):
    data = request.get_json()
    result = update_user(user_id, data)
    if result:
        return jsonify({"message": "User updated"}), 200
    else:
        return jsonify({"error": "User update failed"}), 400

@user_bp.route("/<int:user_id>", methods=["DELETE"])
def del_user(user_id):
    result = delete_user(user_id)
    if result:
        return jsonify({"message":"User Deleted"}), 200
    else:
        return jsonify({"error":"User Deleting Failed"}), 400