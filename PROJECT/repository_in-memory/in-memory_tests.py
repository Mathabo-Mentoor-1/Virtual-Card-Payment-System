from datetime import datetime

# Assuming the User, VirtualCard, and Transaction classes are defined elsewhere

class InMemoryUserRepository:
    def __init__(self):
        self.users = {}

    def create(self, user):
        self.users[user.id] = user
        return user

    def get_by_id(self, user_id):
        return self.users.get(user_id)

    def delete(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False


class InMemoryVirtualCardRepository:
    def __init__(self):
        self.cards = {}

    def create(self, card):
        self.cards[card.id] = card
        return card

    def get_active_cards_by_user(self, user_id):
        return [card for card in self.cards.values() if card.user_id == user_id and card.is_active]

    def get_by_id(self, card_id):
        return self.cards.get(card_id)


class InMemoryTransactionRepository:
    def __init__(self):
        self.transactions = {}

    def create(self, transaction):
        self.transactions[transaction.id] = transaction
        return transaction

    def get_transactions_by_card(self, card_id):
        return [txn for txn in self.transactions.values() if txn.card_id == card_id]


# Simple data classes
class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email


class VirtualCard:
    def __init__(self, id, user_id, card_number, expiration_date, cvv, is_active):
        self.id = id
        self.user_id = user_id
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv
        self.is_active = is_active


class Transaction:
    def __init__(self, id, card_id, amount, timestamp, merchant):
        self.id = id
        self.card_id = card_id
        self.amount = amount
        self.timestamp = timestamp
        self.merchant = merchant


# Shared repository instances for tests
user_repo = InMemoryUserRepository()
card_repo = InMemoryVirtualCardRepository()
transaction_repo = InMemoryTransactionRepository()


# Test CRUD Operations
def test_create_user():
    user = User(id=1, name="Alice", email="alice@example.com")
    created_user = user_repo.create(user)
    assert created_user.id == 1, "Create User failed"
    print(f"User created: {created_user.name}")


def test_create_virtual_card():
    user = user_repo.get_by_id(1)
    if not user:
        user_repo.create(User(id=1, name="Alice", email="alice@example.com"))

    card = VirtualCard(
        id=101,
        user_id=1,
        card_number="4111111111111111",
        expiration_date=datetime(2026, 1, 1),
        cvv="123",
        is_active=True
    )
    created_card = card_repo.create(card)
    assert created_card.id == 101, "Create Virtual Card failed"
    print(f"Virtual Card created for user {created_card.user_id}")


def test_create_transaction():
    if not card_repo.get_by_id(101):
        test_create_virtual_card()

    tx = Transaction(
        id=1001,
        card_id=101,
        amount=99.99,
        timestamp=datetime.now(),
        merchant="Example Store"
    )
    created_tx = transaction_repo.create(tx)
    assert created_tx.id == 1001, "Create Transaction failed"
    print(f"Transaction created: {created_tx.amount} at {created_tx.merchant}")


def test_get_active_cards_by_user():
    # Ensure both cards are created
    card_repo.create(VirtualCard(
        id=101,
        user_id=1,
        card_number="4111111111111111",
        expiration_date=datetime(2026, 1, 1),
        cvv="123",
        is_active=True
    ))
    card_repo.create(VirtualCard(
        id=102,
        user_id=1,
        card_number="4111111111112222",
        expiration_date=datetime(2025, 6, 1),
        cvv="124",
        is_active=False
    ))

    active_cards = card_repo.get_active_cards_by_user(1)
    assert len(active_cards) == 1, "Get Active Cards failed"
    print(f"Active Cards: {len(active_cards)}")


def test_get_transactions_by_card():
    transaction_repo.create(Transaction(
        id=1001,
        card_id=101,
        amount=50.00,
        timestamp=datetime.now(),
        merchant="Example Store"
    ))
    transaction_repo.create(Transaction(
        id=1002,
        card_id=101,
        amount=75.00,
        timestamp=datetime.now(),
        merchant="Another Store"
    ))

    card_txns = transaction_repo.get_transactions_by_card(101)
    assert len(card_txns) == 2, "Get Transactions failed"
    print(f"Transactions for card 101: {len(card_txns)}")


def test_delete_user():
    user_repo.create(User(id=2, name="Bob", email="bob@example.com"))
    deleted = user_repo.delete(2)
    assert deleted is True, "Delete User failed"
    print("User deleted")


if __name__ == "__main__":
    test_create_user()
    test_create_virtual_card()
    test_create_transaction()
    test_get_active_cards_by_user()
    test_get_transactions_by_card()
    test_delete_user()
