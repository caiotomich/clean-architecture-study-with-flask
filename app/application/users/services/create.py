from app.domain.entities.users.exceptions import UnexpectedError, UserNameCannotBeEmpty, UserEmailNotValid, UsersAlreadyExists
from app.application.users.repository import IUserRepository
from app.application.users.dto.create_dto import UserCreateDto

class UserCreate:
    repository: IUserRepository

    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    def execute(self, userCreateDto:UserCreateDto):
        try:
            if self.repository.exists(userCreateDto.email):
                raise UsersAlreadyExists()

            user = userCreateDto.to_entity()
            if user.validated():
                return self.repository.create(user)
        except UserNameCannotBeEmpty as err:
            raise err
        except UsersAlreadyExists as err:
            raise err
        except UserEmailNotValid as err:
            raise err
        except Exception as err:
            print(err)
            raise UnexpectedError()