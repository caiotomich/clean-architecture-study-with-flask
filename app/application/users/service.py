from app.domain.users.exceptions import UnexpectedError, UserNameCannotBeEmpty, UserEmailNotValid
from app.application.users.repository import IUserRepository
from app.application.users.dto import UserCreateDto

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

    def create(self, userDto: UserCreateDto):
        user = userDto.to_entity()

        try:
            if user.validated():
                print("User is valid")
                return self.repository.create(user)
        except UserNameCannotBeEmpty as err:
            raise err
        except UserEmailNotValid as err:
            raise err
        except Exception as err:
            raise UnexpectedError()
