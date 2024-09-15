from app.application.users.repository import IUserRepository
from app.infra.api.models.users import UserModel
from app.domain.entities.users.entity import User
from app.infra.database import db
from datetime import datetime

class UserRepository(IUserRepository):
    def __init__(self):
        self.db = db

    def get_one(self, id) -> User:
        """Get a user from the database."""
        user = self.db.session.query(UserModel).filter_by(id=id).first()

        return User(
            id=user.id,
            name=user.name,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at
        )

    def get_all(self) -> list[User]:
        """Get all users from the database."""
        users = self.db.session.query(UserModel).all()

        return [User(
            id=user.id,
            name=user.name,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at
        ) for user in users]

    def create(self, user):
        """Create a new user in the database."""
        model = UserModel(
            id=user.id,
            name=user.name,
            email=user.email,
            password=user.password,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        self.db.session.add(model)
        self.db.session.commit()

        return model

    def update(self, user: User):
        """Update a user in the database."""
        self.db.session.query(UserModel).filter_by(id=user.id).update({
            'name': user.name,
            'email': user.email,
            'updated_at': user.updated_at
        })
        self.db.session.commit()

        return user

    def delete(self, id):
        """Create a new user in the database."""
        self.db.session.query(UserModel).filter_by(id=id).delete()
        self.db.session.commit()
        return True

    def exists(self, id: str):
        """Get a user from the database and return if it exists or not."""
        user = self.db.session.query(UserModel).filter_by(id=id).first()
        if user is None:
            return False
        return True

    def existsByEmail(self, email: str):
        """Get a user from the database and return if it exists or not."""
        user = self.db.session.query(UserModel).filter_by(email=email).first()
        if user is None:
            return False
        return True