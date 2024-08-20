from app.domain.users.exceptions import UnexpectedError, UserNameCannotBeEmpty, UserEmailNotValid, UserNotFound
from app.application.users.repository import IUserRepository
from app.application.users.dto import UserDto

class UserService(object):
    repository: IUserRepository

    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    def get_one(self, id: str):
        return self.repository.get_one(id)

    # def get_all(self, user_id):
    #     user = user_repository.get_user_by_id(user_id)
    #     if user:
    #         return user
    #     return None

    def create(self, userDto: UserDto):
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

    def update(self, userDto: UserDto):
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

    def delete(self, id: str):
        try:
            if self.repository.exists(id) is False:
                print('User not found')
                raise UserNotFound()
            return self.repository.delete(id)
        except UserNotFound as err:
            raise err
        except Exception as err:
            raise UnexpectedError()