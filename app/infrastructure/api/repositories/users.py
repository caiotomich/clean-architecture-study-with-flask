from app.application.users.repository import IUserRepository
from app.infrastructure.api.models.users import User
from app.infrastructure.database import db

class UserRepository(IUserRepository):
    def __init__(self):
        self.db = db

    def create(self, user):
        """Create a new user in the database."""
        response = User(
            id=user.id,
            name=user.name,
            email=user.email
        )
        self.db.session.add(response)
        self.db.session.commit()

        return response

    def get_one(self, id):
        """Get a user from the database."""
        return self.db.session.query(User).filter_by(id=id).first()
    