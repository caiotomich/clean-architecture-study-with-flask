from app.domain.users.exceptions import UserEmailNotValid, UserNameCannotBeEmpty
from app.domain.users.enums import UserErrorMessagesEnum
import re

class User:
    id: str
    name: str
    email: str

    def __init__(self, id: str, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def validated(self):
        regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not self.email or not re.search(regex, self.email):
            raise UserEmailNotValid()
        elif not self.name:
            raise UserNameCannotBeEmpty()

        return True
