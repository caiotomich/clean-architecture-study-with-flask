from app.domain.entities.users.exceptions import UnexpectedError, UserNameCannotBeEmpty, UserEmailNotValid, UserNotFound
from app.application.users.repository import IUserRepository
from app.application.users.dto.update_dto import UserUpdateDto

class UserUpdate:
    repository: IUserRepository

    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    def execute(self, userDto: UserUpdateDto):
        try:
            user = self.repository.get_one(userDto.id)
            user.name = userDto.name if userDto.name else user.name
            user.email = userDto.email if userDto.email else user.email

            print(user.id, user.name, user.email)

            if self.repository.exists(user.id) is False:
                raise UserNotFound()

            if user.validated():
                return self.repository.update(user)
            return user
        except UserNameCannotBeEmpty as err:
            raise err
        except UserEmailNotValid as err:
            raise err
        except Exception as err:
            raise UnexpectedError()
