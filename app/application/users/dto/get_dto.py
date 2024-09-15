from app.domain.entities.users.entity import User

class UserGetDto(object):
    def __init__(self, user: User):
        self.id = user.id
        self.name = user.name
        self.email = user.email
        self.created_at = user.created_at.isoformat()
        self.updated_at = user.updated_at.isoformat()

    def data(self) -> object:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
