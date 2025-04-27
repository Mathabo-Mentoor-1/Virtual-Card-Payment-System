from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')
ID = TypeVar('ID')

class IRepository(ABC, Generic[T, ID]):

    @abstractmethod
    def create(self, entity: T) -> T:
        pass

    @abstractmethod
    def read(self, entity_id: ID) -> Optional[T]:
        pass

    @abstractmethod
    def update(self, entity: T) -> T:
        pass

    @abstractmethod
    def delete(self, entity_id: ID) -> None:
        pass

    @abstractmethod
    def list_all(self) -> List[T]:
        pass

