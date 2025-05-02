import uuid
from datetime import datetime
from models import User, VirtualCard, Transaction
from interfaces import IUserService, ICardService, ITransactionService
from repository import IRepository
from typing import List

class UserService(IUserService):
    def __init__(self, repo: IRepository[User]):
        self.repo = repo

    def create_user(self, name: str, email: str) -> User:
        user = User(id=str(uuid.uuid4()), name=name, email=email)
        self.repo.add(user)
        return user

class CardService(ICardService):
    def __init__(self, repo: IRepository[VirtualCard]):
        self.repo = repo

    def issue_card(self, user_id: str) -> VirtualCard:
        card = VirtualCard(
            id=str(uuid.uuid4()),
            user_id=user_id,
            card_number=str(uuid.uuid4().int)[:16],
            expiry_date="12/30",
            balance=1000.0
        )
        self.repo.add(card)
        return card

    def get_user_cards(self, user_id: str) -> List[VirtualCard]:
        return [card for card in self.repo.get_all() if card.user_id == user_id]

class TransactionService(ITransactionService):
    def __init__(self, card_repo: IRepository[VirtualCard], txn_repo: IRepository[Transaction]):
        self.card_repo = card_repo
        self.txn_repo = txn_repo

    def make_payment(self, card_id: str, amount: float, description: str) -> Transaction:
        card = self.card_repo.get_by_id(card_id)
        if not card:
            raise ValueError("Card not found")
        if card.balance < amount:
            raise ValueError("Insufficient funds")

        card.balance -= amount
        self.card_repo.update(card)

        txn = Transaction(
            id=str(uuid.uuid4()),
            card_id=card_id,
            amount=amount,
            timestamp=datetime.utcnow(),
            description=description
        )
        self.txn_repo.add(txn)
        return txn

    def get_card_transactions(self, card_id: str) -> List[Transaction]:
        return [txn for txn in self.txn_repo.get_all() if txn.card_id == card_id]
