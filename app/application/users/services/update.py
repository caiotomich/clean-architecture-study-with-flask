from app.domain.users.exceptions import UnexpectedError, UserNameCannotBeEmpty, UserEmailNotValid
from app.application.users.repository import IUserRepository
from app.application.users.dto.create_dto import UserCreateDto

class UserUpdate:
    repository: IUserRepository

    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    @staticmethod
    def execute(self, userDto: UserCreateDto):
        try:
            user = self.repository.get_one(userDto.id)
            user.name = userDto.name if userDto.name else user.name
            user.email = userDto.email if userDto.email else user.email

            if user.validated():
                return self.repository.update(user)
        except UserNameCannotBeEmpty as err:
            raise err
        except UserEmailNotValid as err:
            raise err
        except Exception as err:
            print(err)
            raise UnexpectedError()
