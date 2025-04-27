from typing import List, Dict, Generic, TypeVar, Optional
from datetime import datetime
from dataclasses import dataclass

T = TypeVar('T')
K = TypeVar('K')

# Base in-memory repository
class InMemoryRepository(Generic[T, K]):
    def __init__(self):
        self._storage: Dict[K, T] = {}

    def create(self, entity: T) -> T:
        entity_id = getattr(entity, 'id', None)
        if entity_id is None:
            raise ValueError("Entity must have an 'id' attribute")
        self._storage[entity_id] = entity
        return entity

    def get(self, id: K) -> Optional[T]:
        return self._storage.get(id)

# Entity definitions
@dataclass
class User:
    id: int
    name: str
    email: str

@dataclass
class VirtualCard:
    id: int
    user_id: int
    card_number: str
    expiration_date: datetime
    cvv: str
    is_active: bool

@dataclass
class Transaction:
    id: int
    card_id: int
    amount: float
    timestamp: datetime
    merchant: str

# Dummy interfaces (for illustration)
class IUserRepository: pass
class IVirtualCardRepository: pass
class ITransactionRepository: pass

# In-Memory Repositories
class InMemoryUserRepository(InMemoryRepository[User, int], IUserRepository):
    pass

class InMemoryVirtualCardRepository(InMemoryRepository[VirtualCard, int], IVirtualCardRepository):
    def get_active_cards_by_user(self, user_id: int) -> List[VirtualCard]:
        return [
            card for card in self._storage.values()
            if card.user_id == user_id and card.is_active
        ]

class InMemoryTransactionRepository(InMemoryRepository[Transaction, int], ITransactionRepository):
    def get_transactions_by_card(self, card_id: int) -> List[Transaction]:
        return [
            tx for tx in self._storage.values()
            if tx.card_id == card_id
        ]

# Usage
if __name__ == "__main__":
    user_repo = InMemoryUserRepository()
    card_repo = InMemoryVirtualCardRepository()
    transaction_repo = InMemoryTransactionRepository()

    # Add a user
    user = user_repo.create(User(id=1, name="Alice", email="alice@example.com"))

    # Add a virtual card
    card = card_repo.create(VirtualCard(
        id=101,
        user_id=1,
        card_number="4111111111111111",
        expiration_date=datetime(2026, 1, 1),
        cvv="123",
        is_active=True
    ))

    # Record a transaction
    tx = transaction_repo.create(Transaction(
        id=1001,
        card_id=101,
        amount=99.99,
        timestamp=datetime.now(),
        merchant="Example Store"
    ))

    # Fetch active cards for a user
    active_cards = card_repo.get_active_cards_by_user(1)
    print("Active cards:", active_cards)

    # Fetch transactions for a card
    card_txns = transaction_repo.get_transactions_by_card(101)
    print("Transactions:", card_txns)
