from app.domain.entities.users.exceptions import UserEmailNotValid, UserNameCannotBeEmpty
import re

class User:
    id: str
    name: str
    email: str
    password: str

    def __init__(self, id: str, name: str, email: str, password: str):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def validated(self):
        regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not self.email or not re.search(regex, self.email):
            raise UserEmailNotValid()
        elif not self.name:
            raise UserNameCannotBeEmpty()

        return True

    def check_password(self, password):
        return self.password == password