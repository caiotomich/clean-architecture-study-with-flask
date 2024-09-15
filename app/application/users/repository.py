from abc import ABC, abstractmethod
from app.domain.entities.users.entity import User

class IUserRepository(ABC):
    @abstractmethod
    def get_one(self, id: str) -> User:
        ...

    @abstractmethod
    def get_all(self) -> list[User]:
        ...

    @abstractmethod
    def create(self, name: str, email: str, password: str) -> User:
        ...

    @abstractmethod
    def update(self, user: User) -> User:
        ...

    @abstractmethod
    def delete(self, id) -> User:
        ...

    @abstractmethod
    def exists(self, id=None) -> User:
        ...

    @abstractmethod
    def existsByEmail(self, email=None) -> User:
        ...
