from config import DB_CONFIG
from app.models import create_user_query, get_user_query, update_user_query, delete_user_query

def create_user(data):
    try:
        # (with) is shorter, cleaner, and automatically closes the cursor when the block is done.
        # (cursor) which is used to execute SQL queries
        with DB_CONFIG.cursor() as cursor:
            values = (data["first_name"], data["last_name"], data["username"], data["email"], data["password"]) 
            cursor.execute(create_user_query(), values)
            DB_CONFIG.commit()
            # Returns the ID of the newly created user (auto-incremented primary key).
            return cursor.lastrowid
    except Exception as e:
        # print("Error creating user:", e)
        return None
    
def get_user(user_id):
    try:
        with DB_CONFIG.cursor() as cursor:
            cursor.execute(get_user_query(), (user_id,))
            return cursor.fetchone()
    except Exception as e:
        # print("error in getting user:", e)
        return None
    
def update_user(user_id, data):
    try:
        with DB_CONFIG.cursor() as cursor:
            values = (data["first_name"], data["last_name"], data["username"], data["email"], data["password"], user_id)
            cursor.execute(update_user_query(), values)
            DB_CONFIG.commit()
            return cursor.rowcount
    except Exception as e:
        # print("Error in updating:", e)
        return None

def delete_user(user_id):
    try: 
        with DB_CONFIG.cursor() as cursor:
            cursor.execute(delete_user_query(), user_id)
            DB_CONFIG.commit()
            return cursor.rowcount
    except Exception as e:
        # print("Error in deleting:", e)
        return None