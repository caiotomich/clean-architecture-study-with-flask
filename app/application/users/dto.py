from app.domain.users.entity import User
from uuid import uuid4

class UserDto(object):
    def __init__(self, name: str, email: str, id: str=None):
        self.id = id if id else str(uuid4())
        self.name = name
        self.email = email

    def to_entity(self):
        return User(
            id=self.id,
            name=self.name,
            email=self.email
        )

class UserUpdateDto(object):
    def __init__(self, name: str, email: str=None, id: str=None):
        self.id = id if id else str(uuid4())
        self.name = name
        self.email = email

    def to_entity(self):
        return User(
            id=self.id,
            name=self.name,
            email=self.email
        )

