from app.domain.entities.users.entity import User
from datetime import datetime
from uuid import uuid4

class UserUpdateDto(object):
    def __init__(self, id: str, name: str, email: str):
        self.id = id if id else str(uuid4())
        self.name = name
        self.email = email
        self.updated_at = datetime.now()

    def to_entity(self):
        return User(
            id=self.id,
            name=self.name,
            email=self.email,
            updated_at = self.updated_at
        )

