from app.domain.users.entity import User
from uuid import uuid4

class UserCreateDto(object):
    def __init__(self, name, email):
        self.id = str(uuid4())
        self.name = name
        self.email = email

    def to_entity(self):
        return User(
            id=self.id,
            name=self.name,
            email=self.email
        )

class UserDto(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_entity(self):
        return User(
            id=self.id,
            name=self.name,
            email=self.email
        )


