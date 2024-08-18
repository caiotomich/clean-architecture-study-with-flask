from app.infrastructure.models.user import UserModel
import uuid

class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        """Retrieve a user by their ID."""
        return UserModel.query.all()

    def get_one(self, id):
        """Retrieve a user by their ID."""
        return UserModel.query.get(id)

    def create_user(self, name, email):
        """Create a new user in the database."""
        new_user = UserModel(id=str(uuid.uuid4()), name=name, email=email)
        self.db.session.add(new_user)
        self.db.session.commit()
        return new_user

    def update_user(self, id, name=None, email=None):
        """Update an existing user."""
        user = self.get_one(id)
        if user:
            if name:
                user.name = name
            if email:
                user.email = email
            self.db.session.commit()
        return user

    def delete_user(self, id):
        """Delete a user from the database."""
        user = self.get_one(id)
        if user:
            self.db.session.delete(user)
            self.db.session.commit()
        return user