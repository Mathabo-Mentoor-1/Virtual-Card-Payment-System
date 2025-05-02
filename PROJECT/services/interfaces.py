from abc import ABC, abstractmethod
from typing import List
from models import User, VirtualCard, Transaction

class IUserService(ABC):
    @abstractmethod
    def create_user(self, name: str, email: str) -> User: pass

class ICardService(ABC):
    @abstractmethod
    def issue_card(self, user_id: str) -> VirtualCard: pass

    @abstractmethod
    def get_user_cards(self, user_id: str) -> List[VirtualCard]: pass

class ITransactionService(ABC):
    @abstractmethod
    def make_payment(self, card_id: str, amount: float, description: str) -> Transaction: pass

    @abstractmethod
    def get_card_transactions(self, card_id: str) -> List[Transaction]: pass
