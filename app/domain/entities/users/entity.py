from app.domain.entities.users.exceptions import UserEmailNotValid, UserNameCannotBeEmpty
from datetime import datetime
import re

class User:
    id: str
    name: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime

    def __init__(
        self,
        id: str,
        name: str,
        email: str,
        password: str = None,
        created_at: datetime=None,
        updated_at: datetime=None
    ):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()

    def validated(self):
        regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not self.email or not re.search(regex, self.email):
            raise UserEmailNotValid()
        elif not self.name:
            raise UserNameCannotBeEmpty()

        return True

    def check_password(self, password):
        return self.password == password