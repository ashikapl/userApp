from flask import Flask, jsonify, request, Blueprint
from app.services.user import *

user_bp = Blueprint('user_bp', __name__)

@user_bp.route("/", methods=["POST"])
def add_user():
    data = request.get_json()
    result = add_user_service(data)
    if result["success"]:
        return jsonify({"message": "User Created", "user_id":result["user_id"]}), 201
    else:
        return jsonify({"error":result["error"]}), 400

@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = read_user_service(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User Not Found!"}),404                                  

@user_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    result = update_user_service(user_id, data)
    if result["success"]:
        return jsonify({"message": "User updated"}), 200
    else:
        return jsonify({"error": result["error"]}), 400

@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    result = delete_user_service(user_id)
    if result["success"]:
        return jsonify({"message":"User Deleted"}), 200
    else:
        return jsonify({"error":"User Not Found!"}), 400