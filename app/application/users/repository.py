from abc import ABC, abstractmethod
from app.domain.entities.users.entity import User

class IUserRepository(ABC):
    @abstractmethod
    def get_one(self, id: str) -> User:
        ...

    # @abstractmethod
    # def get_all(self) -> List[User]:
    #     ...

    @abstractmethod
    def create(self, name: str, email: str) -> User:
        ...

    @abstractmethod
    def update(self, id, name=None, email=None) -> User:
        ...

    # @abstractmethod
    # def delete(self, id) -> User:
    #     ...
