class User:
    def __init__(self, user_id, first_name, last_name, username, email, password):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name 
        self.username = username
        self.email  = email
        self.password = password

    def to_dict(self):
        return{
            "user_id":self.user_id,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "username":self.username,
            "email":self.email,
            "password":self.password
        }
        