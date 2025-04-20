from datetime import datetime
from typing import List
import uuid


class User:
    def __init__(self, user_id: str, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.cards: List[VirtualCard] = []

    def create_virtual_card(self, issuer: 'CardIssuer', limit: float, expiry_date: str):
        card = issuer.issue_card(self, limit, expiry_date)
        self.cards.append(card)
        return card

    def __str__(self):
        return f"User({self.name}, {self.email})"


class VirtualCard:
    def __init__(self, card_number: str, user: User, limit: float, expiry_date: str):
        self.card_number = card_number
        self.user = user
        self.limit = limit
        self.expiry_date = expiry_date
        self.balance = limit
        self.transactions: List[Transaction] = []

    def authorize_payment(self, amount: float, merchant: str):
        if amount <= self.balance:
            transaction = Transaction(self, amount, merchant)
            self.balance -= amount
            self.transactions.append(transaction)
            return transaction
        else:
            raise ValueError("Insufficient card balance")

    def __str__(self):
        return f"VirtualCard({self.card_number}, Balance: {self.balance})"


class Transaction:
    def __init__(self, card: VirtualCard, amount: float, merchant: str):
        self.transaction_id = str(uuid.uuid4())
        self.card = card
        self.amount = amount
        self.merchant = merchant
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Transaction({self.amount} to {self.merchant} on {self.timestamp})"


class CardIssuer:
    def __init__(self, issuer_name: str):
        self.issuer_name = issuer_name
        self.issued_cards: List[VirtualCard] = []

    def issue_card(self, user: User, limit: float, expiry_date: str) -> VirtualCard:
        card_number = self.generate_card_number()
        card = VirtualCard(card_number, user, limit, expiry_date)
        self.issued_cards.append(card)
        return card

    def generate_card_number(self) -> str:
        return str(uuid.uuid4()).replace('-', '')[:16]

    def __str__(self):
        return f"CardIssuer({self.issuer_name})"


class PaymentGateway:
    def __init__(self):
        self.transactions: List[Transaction] = []

    def process_payment(self, card: VirtualCard, amount: float, merchant: str):
        try:
            transaction = card.authorize_payment(amount, merchant)
            self.transactions.append(transaction)
            print(f"Payment successful: {transaction}")
            return transaction
        except ValueError as e:
            print(f"Payment failed: {e}")
            return None

    def __str__(self):
        return f"PaymentGateway({len(self.transactions)} transactions processed)"
