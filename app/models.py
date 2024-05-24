from app import mongo, login_manager,bcrypt
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, user_name, email, password):
        self.user_name = user_name
        self.email = email
        self.password = password
        self.id = id

    def get_id(self):
           return (self.id)
    
    @staticmethod
    def get_user(email):
        user_data = mongo.db.users.find_one({"email": email})
        if user_data:
            return User(str(user_data['_id']),user_data['user_name'], user_data['email'], user_data['password'])
        return None
    
    @staticmethod
    def create_user(user_name, email, password):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = { "user_name": user_name,"email": email,"password": hashed_password}
        res = mongo.db.users.insert_one(user)

        return User(str(res.inserted_id), user_name, email, hashed_password)
    

