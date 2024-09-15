from app.domain.entities.users.enums import UserErrorMessagesEnum

class UnexpectedError(Exception):
    def __init__(self, message=None):
        self.message = message if message else UserErrorMessagesEnum.UNEXPECTED_ERROR.value
        self.code = 'UNEXPECTED_ERROR'

class UserNameCannotBeEmpty(Exception):
    def __init__(self, message=None):
        self.message = message if message else UserErrorMessagesEnum.USER_NAME_CANNOT_BE_EMPTY.value
        self.code = 'USER_NAME_CANNOT_BE_EMPTY'

class UserEmailNotValid(Exception):
    def __init__(self, message=None):
        self.message = message if message else UserErrorMessagesEnum.USER_EMAIL_NOT_VALID.value
        self.code = 'USER_EMAIL_NOT_VALID'

class UserNotFound(Exception):
    def __init__(self, message=None):
        self.message = message if message else UserErrorMessagesEnum.USER_NOT_FOUND.value
        self.code = 'USER_NOT_FOUND'

class UsersAlreadyExists(Exception):
    def __init__(self, message=None):
        self.message = message if message else UserErrorMessagesEnum.USER_ALREADY_EXISTS.value
        self.code = 'USER_ALREADY_EXISTS'

# class UserNotValid(Exception):
#     def __init__(self, message=None):
#         self.message = message if message else UserErrorMessagesEnum.USER_NOT_VALID.value
#         self.code = 'USER_NOT_VALID'

# class UserEmailAlreadyExists(Exception):
#     def __init__(self, message=None):
#         self.message = message if message else UserErrorMessagesEnum.USER_EMAIL_NOT_VALID.value
#         self.code = 'USER_EMAIL_NOT_VALID'


