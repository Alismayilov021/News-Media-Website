from app.models.user import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:

    @staticmethod
    def get_all_users():
        # Retrieve all users from the database
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        # Retrieve a user by their ID, returns None if not found
        return User.query.get(user_id)

    @staticmethod
    def create_user(data):
        # Hash the password before saving
        hashed_password = generate_password_hash(data['password'], method='sha256')

        user = User(
            username=data['username'],
            email=data['email'],
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update_user(user_id, data):
        # Find the user by ID
        user = User.query.get(user_id)

        if 'username' in data:
            user.username = data['username']
        if 'email' in data:
            user.email = data['email']
        if 'password' in data:
            user.password = generate_password_hash(data['password'], method='sha256')

        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        # Retrieve and delete a user by ID
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
