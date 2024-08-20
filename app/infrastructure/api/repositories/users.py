from app.application.users.repository import IUserRepository
from app.infrastructure.api.models.users import UserModel
from app.domain.users.entity import User
from app.infrastructure.database import db

class UserRepository(IUserRepository):
    def __init__(self):
        self.db = db

    def get_one(self, id) -> User:
        """Get a user from the database."""
        user = self.db.session.query(UserModel).filter_by(id=id).first()

        return User(
            id=user.id,
            name=user.name,
            email=user.email
        )

    def create(self, user):
        """Create a new user in the database."""
        model = UserModel(
            id=user.id,
            name=user.name,
            email=user.email
        )
        self.db.session.add(model)
        self.db.session.commit()

        return model
    
    def update(self, user):
        """Create a new user in the database."""
        UserModel.query.update({UserModel.name: user.name, UserModel.email: user.email})
        # user = self.db.session.query(UserModel).filter_by(id=user.id).first()
        # user.name = user.name
        # user.email = user.email
        self.db.session.commit()

        return user
    