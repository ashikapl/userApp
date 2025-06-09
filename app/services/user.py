from app.store.user import *

def add_user_service(data):
    try:
        user_id = add_user_store(data)  # DB function returns user ID
        return {"success": True, "user_id": user_id}
    except Exception as e:
        return {"success": False, "error": str(e)}

def read_user_service(user_id):
    try:
        data = get_user_store(user_id)
        return data
    except Exception as e:
        return str(e)

def update_user_service(user_id, data):
    try:
        rowCount = update_user_store(user_id, data)
        if rowCount == 0:
            return {"success": False, "error": "User not found"}

        return {"success": True, "rowCount_deleted": rowCount}

    except Exception as e:
        return {"success": False, "error": str(e)}

def delete_user_service(user_id):
    try:
        rowCount_deleted = delete_user_store(user_id)  # from model

        if rowCount_deleted == 0:
            return {"success": False, "error": "User not found"}

        return {"success": True, "rowCount_deleted": rowCount_deleted}

    except Exception as e:
        return {"success": False, "error": str(e)}
