from typing import TypeVar, Generic, Optional, List, Dict
from abc import ABC, abstractmethod

T = TypeVar('T')

# Define a simple interface for IRepository
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

# In-memory implementation
class InMemoryRepository(IRepository[T]):
    def __init__(self):
        self._entities: Dict[str, T] = {}

    def get_by_id(self, id: str) -> Optional[T]:
        return self._entities.get(id)

    def get_all(self) -> List[T]:
        return list(self._entities.values())

    def add(self, entity: T) -> None:
        self._entities[entity.id] = entity

    def update(self, entity: T) -> None:
        self._entities[entity.id] = entity

    def delete(self, id: str) -> None:
        if id in self._entities:
            del self._entities[id]

