from typing import Dict, Generic, TypeVar, Optional, List

# Define generic type variables
T = TypeVar('T')
ID = TypeVar('ID')

# Dummy interface for IRepository to make the code complete
class IRepository(Generic[T, ID]):
    def create(self, entity: T) -> T: ...
    def read(self, entity_id: ID) -> Optional[T]: ...
    def update(self, entity: T) -> T: ...
    def delete(self, entity_id: ID) -> None: ...
    def list(self) -> List[T]: ...

class InMemoryRepository(IRepository[T, ID], Generic[T, ID]):
    def __init__(self):
        self._storage: Dict[ID, T] = {}

    def create(self, entity: T) -> T:
        self._storage[getattr(entity, "id")] = entity
        return entity

    def read(self, entity_id: ID) -> Optional[T]:
        return self._storage.get(entity_id)

    def update(self, entity: T) -> T:
        self._storage[getattr(entity, "id")] = entity
        return entity

    def delete(self, entity_id: ID) -> None:
        if entity_id in self._storage:
            del self._storage[entity_id]

    def list(self) -> List[T]:
        return list(self._storage.values())

