from app.domain.entities.users.exceptions import UnexpectedError, UserNotFound
from app.application.users.repository import IUserRepository
from app.application.users.dto.get_dto import UserGetDto

class UserGetOne:
    repository: IUserRepository

    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    def execute(self, id: str):
        try:
            if self.repository.exists(id) is False:
                raise UserNotFound()
            return self.repository.get_one(id)
        except UserNotFound as err:
            raise err
        except Exception as err:
            raise UnexpectedError()
