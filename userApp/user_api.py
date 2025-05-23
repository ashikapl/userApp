from flask import Flask, request, jsonify
from dotenv import load_dotenv
import pymysql
import os

# Load environment variables
load_dotenv()

user_api = Flask( __name__)

# Connect to user database
user_db = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

user_cursor = user_db.cursor()

#----------------------------User Crud Api----------------------------------------
# create user data
@user_api.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    query = "INSERT INTO user_table(first_name, last_name, username, email, password) VALUES (%s, %s, %s, %s, %s)"
    values = (data["first_name"], data["last_name"], data["username"], data["email"], data["password"])
    user_cursor.execute(query, values)
    user_db.commit()
    return jsonify({"message":"User created!"})
                                   
# read user data
@user_api.route("/",methods=["GET"])
def read_user1():
    user_cursor.execute("SELECT * FROM user_table")
    user = user_cursor.fetchall()
    return jsonify(user)

# Get method 2 (by using user id)
@user_api.route("/<int:user_id>", methods=["GET"])
def read_user2(user_id):
    user_cursor.execute("SELECT * FROM user_table WHERE user_id = %s", (user_id))
    user = user_cursor.fetchone()
    return jsonify(user)
 
# update user data
@user_api.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    query = "UPDATE user_table SET first_name=%s, last_name=%s, username=%s, email=%s, password=%s WHERE user_id=%s"
    values = (data["first_name"], data["last_name"], data["username"], data["email"], data["password"], (user_id))
    user_cursor.execute(query, values)
    user_db.commit()
    return jsonify({"message":"User Updated!"}), 200

# Delete user data
@user_api.route("/<int:user_id>", methods=["DELETE"])
def del_user(user_id):
    user_cursor.execute("SELECT * FROM user_table WHERE user_id=%s", (user_id))
    user = user_cursor.fetchone()

    if not user:
        return jsonify({"message":"User Not Found!"}), 404
    
    user_cursor.execute("DELETE FROM user_table WHERE user_id=%s", (user_id))
    user_db.commit()
    return jsonify({"message":"User Deleted!"}), 200

if __name__ == "__main__":
    user_api.run(port=8000, debug=True)