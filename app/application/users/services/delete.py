from app.domain.entities.users.exceptions import UnexpectedError, UserNotFound
from app.application.users.repository import IUserRepository

class UserDelete:
    repository: IUserRepository

    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    @staticmethod
    def execute(self, id: str):
        try:
            if self.repository.exists(id) is False:
                print('User not found')
                raise UserNotFound()
            return self.repository.delete(id)
        except UserNotFound as err:
            raise err
        except Exception as err:
            raise UnexpectedError()