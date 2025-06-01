def create_user_query():
    return "INSERT INTO user_table(first_name, last_name, username, email, password) VALUES (%s, %s, %s, %s, %s)"

def get_user_query():
    return "SELECT * FROM user_table WHERE user_id = %s"

def update_user_query():
    return "UPDATE user_table SET first_name=%s, last_name=%s, username=%s, email=%s, password=%s WHERE user_id=%s"

def delete_user_query():
    return "DELETE FROM user_table WHERE user_id=%s"