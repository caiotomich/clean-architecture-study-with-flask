from app.application.users.repository import IUserRepository

class UserGetOne:
    repository: IUserRepository

    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    @staticmethod
    def execute(self, id: str):
        return self.repository.get_one(id)

    # def get_all(self, user_id):
    #     user = user_repository.get_user_by_id(user_id)
    #     if user:
    #         return user
    #     return None