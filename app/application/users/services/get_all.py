from app.application.users.repository import IUserRepository

class UserGetAll:
    repository: IUserRepository

    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    def execute(self):
        return self.repository.get_all()
