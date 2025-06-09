from app.models.user import User
from config import DB_CONFIG

def add_user_store(data):
        with DB_CONFIG.cursor() as cursor:
            query = "INSERT INTO User(first_name, last_name, username, email, password) VALUES (%s, %s, %s, %s, %s)"
            values = (data["first_name"], data["last_name"], data["username"], data["email"], data["password"]) 
            cursor.execute(query, values)
            DB_CONFIG.commit()
            return cursor.lastrowid
    
def get_user_store(user_id):
        with DB_CONFIG.cursor() as cursor:
            cursor.execute("SELECT * FROM User WHERE user_id = %s", user_id)
            return cursor.fetchone()
    
def update_user_store(user_id, data):
        with DB_CONFIG.cursor() as cursor:
            query = "UPDATE User SET first_name=%s, last_name=%s, username=%s, email=%s, password=%s WHERE user_id=%s"
            values = (data["first_name"], data["last_name"], data["username"], data["email"], data["password"], user_id)
            cursor.execute(query, values)
            DB_CONFIG.commit()
            return cursor.rowcount

def delete_user_store(user_id):
        with DB_CONFIG.cursor() as cursor:
            cursor.execute("DELETE FROM User WHERE user_id=%s", user_id)
            DB_CONFIG.commit()
            return cursor.rowcount