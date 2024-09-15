from app.domain.entities.users.entity import User
from uuid import uuid4

class UserCreateDto(object):
    def __init__(self, name: str, email: str, password: str = None, id: str=None):
        self.id = id if id else str(uuid4())
        self.name = name
        self.email = email
        self.password = password

    def to_entity(self):
        return User(
            id=self.id,
            name=self.name,
            email=self.email,
            password=self.password
        )
