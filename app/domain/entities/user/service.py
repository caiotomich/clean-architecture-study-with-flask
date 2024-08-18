from app.infrastructure.api import db
from app.domain.entities.user.entity import User
from app.domain.entities.user.repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository(db)

    def get_all(self):
        """Retrieve all users and map to entity."""
        return self.user_repository.get_all()

    def get_user(self, id):
        """Retrieve a user by their ID and map to entity."""
        user_model = self.user_repository.get_user_by_id(id)
        if user_model:
            return User(
                id=user_model.id,
                name=user_model.name,
                email=user_model.email
            )
        return None

    def create_user(self, name, email):
        """Create a new user and map to entity."""
        user_model = self.user_repository.create_user(name, email)
        return User(
            id=user_model.id,
            name=user_model.name,
            email=user_model.email
        )

    def update_user(self, id, name=None, email=None):
        """Update an existing user."""
        user_model = self.user_repository.update_user(id, name, email)
        if user_model:
            return User(
                id=user_model.id,
                name=user_model.name,
                email=user_model.email
            )
        return None

    def delete_user(self, uuid):
        """Delete a user by their ID."""
        user = self.user_repository.delete_user(uuid)
        if user:
            return User(
                id=user.id,
                name=user.name,
                email=user.email
            )
        return None
