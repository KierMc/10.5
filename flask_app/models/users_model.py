from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('users_schema').query_db(query)

        users = []

        for user in results:
            instance=cls(user)
            users.append(instance)

        return users
    
    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, created_at)'
        query += "VALUES(%(first_name)s, %(last_name)s, %(email)s, NOW())"
        new_user_id = connectToMySQL('users_schema').query_db(query,data)
        return new_user_id