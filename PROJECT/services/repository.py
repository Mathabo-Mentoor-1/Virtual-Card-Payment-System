from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')

class IRepository(ABC, Generic[T]):
    @abstractmethod
    def get_by_id(self, id: str) -> Optional[T]: pass

    @abstractmethod
    def get_all(self) -> List[T]: pass

    @abstractmethod
    def add(self, entity: T) -> None: pass

    @abstractmethod
    def update(self, entity: T) -> None: pass

    @abstractmethod
    def delete(self, id: str) -> None: pass
