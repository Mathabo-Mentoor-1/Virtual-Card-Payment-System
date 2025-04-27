from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

# Type variables for entity and ID types
T = TypeVar('T')  # Entity type
ID = TypeVar('ID')  # ID type

# Base Repository Interface
class IRepository(ABC, Generic[T, ID]):
    @abstractmethod
    def add(self, entity: T):
        pass

    @abstractmethod
    def remove(self, entity: T):
        pass

    @abstractmethod
    def get(self, id: ID) -> T:
        pass

# Dummy entity class declarations for type hints
class User:
    pass

class VirtualCard:
    pass

class Transaction:
    pass

# Specific repository interfaces
class IUserRepository(IRepository[User, int], ABC):
    pass  # Add user-specific methods if needed

class IVirtualCardRepository(IRepository[VirtualCard, int], ABC):
    @abstractmethod
    def get_active_cards_by_user(self, user_id: int) -> List[VirtualCard]:
        pass

class ITransactionRepository(IRepository[Transaction, int], ABC):
    @abstractmethod
    def get_transactions_by_card(self, card_id: int) -> List[Transaction]:
        pass


