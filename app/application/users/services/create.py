from app.domain.entities.users.exceptions import UnexpectedError, UserNameCannotBeEmpty, UserEmailNotValid
from app.application.users.repository import IUserRepository
from app.application.users.dto.create_dto import UserCreateDto

class UserCreate:
    repository: IUserRepository

    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    @staticmethod
    def execute(self, userDto: UserCreateDto):
        try:
            user = userDto.to_entity()
            if user.validated():
                return self.repository.create(user)
        except UserNameCannotBeEmpty as err:
            raise err
        except UserEmailNotValid as err:
            raise err
        except Exception as err:
            raise UnexpectedError()