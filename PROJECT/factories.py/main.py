# Payment Model
class Payment:
    def __init__(self, card_number: str, amount: float, currency: str, payment_status: str):
        self.card_number = card_number
        self.amount = amount
        self.currency = currency
        self.payment_status = payment_status

    def __repr__(self):
        return f"Payment({self.card_number}, {self.amount}, {self.currency}, {self.payment_status})"


# Storage Interface
from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save_payment(self, payment: Payment) -> None:
        pass

    @abstractmethod
    def get_payment(self, card_number: str) -> Payment:
        pass


# SQL Storage
class SQLStorage(Storage):
    def __init__(self):
        self.payments_db = {}

    def save_payment(self, payment: Payment) -> None:
        # Simulate saving payment to SQL
        self.payments_db[payment.card_number] = payment
        print(f"Saving payment {payment} to SQL database")

    def get_payment(self, card_number: str) -> Payment:
        # Simulate retrieving payment from SQL
        return self.payments_db.get(card_number, None)


# NoSQL Storage
class NoSQLStorage(Storage):
    def __init__(self):
        self.payments_db = {}

    def save_payment(self, payment: Payment) -> None:
        # Simulate saving payment to NoSQL database
        self.payments_db[payment.card_number] = payment
        print(f"Saving payment {payment} to NoSQL database")

    def get_payment(self, card_number: str) -> Payment:
        # Simulate retrieving payment from NoSQL
        return self.payments_db.get(card_number, None)


# In-Memory Storage
class InMemoryStorage(Storage):
    def __init__(self):
        self.payments_db = {}

    def save_payment(self, payment: Payment) -> None:
        # Simulate saving payment in memory
        self.payments_db[payment.card_number] = payment
        print(f"Saving payment {payment} to in-memory storage")

    def get_payment(self, card_number: str) -> Payment:
        # Simulate retrieving payment from in-memory storage
        return self.payments_db.get(card_number, None)


# Storage Factory
class StorageFactory:
    @staticmethod
    def get_storage(storage_type: str) -> Storage:
        if storage_type == "SQL":
            return SQLStorage()
        elif storage_type == "NoSQL":
            return NoSQLStorage()
        elif storage_type == "InMemory":
            return InMemoryStorage()
        else:
            raise ValueError("Unknown storage type")


# Payment Repository
class PaymentRepository:
    def __init__(self, storage: Storage):
        self.storage = storage

    def save_payment(self, payment: Payment) -> None:
        self.storage.save_payment(payment)

    def get_payment(self, card_number: str) -> Payment:
        payment = self.storage.get_payment(card_number)
        if payment is None:
            print(f"Payment with card number {card_number} not found.")
        return payment


# Usage Example
def main():
    # Get storage from the factory
    storage_type = "SQL"  # You can change this to "NoSQL", "InMemory" as needed
    storage = StorageFactory.get_storage(storage_type)
    
    # Initialize the repository with the chosen storage
    payment_repo = PaymentRepository(storage)

    # Create a payment
    payment = Payment("1234-5678-9876-5432", 100, "USD", "Pending")
    
    # Save the payment
    payment_repo.save_payment(payment)
    
    # Retrieve the payment
    retrieved_payment = payment_repo.get_payment("1234-5678-9876-5432")
    if retrieved_payment:
        print(f"Retrieved payment: {retrieved_payment}")
    else:
        print("Payment not found.")

if __name__ == "__main__":
    main()
