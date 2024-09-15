from enum import Enum

class UserErrorMessagesEnum(Enum):
    UNEXPECTED_ERROR = "Erro inesperado, contate o suporte."
    USER_NAME_CANNOT_BE_EMPTY = "User name cannot be empty"
    USER_EMAIL_NOT_VALID = "User email not valid"
    USER_ALREADY_EXISTS = "User already exists"
    USER_NOT_VALID = "User not valid"
    USER_NOT_FOUND = "User not found"