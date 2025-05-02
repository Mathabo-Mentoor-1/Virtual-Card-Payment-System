class VirtualCard:
    def __init__(self, card_id, user_id, balance):
        self.card_id = card_id
        self.user_id = user_id
        self.balance = balance

class VirtualCardRepository:
    def get_card_by_id(self, card_id):
        pass

    def save_card(self, card):
        pass


from abc import ABC, abstractmethod

class IVirtualCardService(ABC):
    @abstractmethod
    def get_balance(self, card_id): pass

    @abstractmethod
    def debit(self, card_id, amount): pass


from interfaces import IVirtualCardService

class VirtualCardService(IVirtualCardService):
    def __init__(self, repository):
        self.repository = repository

    def get_balance(self, card_id):
        card = self.repository.get_card_by_id(card_id)
        if not card:
            raise ValueError("Card not found")
        return card.balance

    def debit(self, card_id, amount):
        card = self.repository.get_card_by_id(card_id)
        if not card:
            raise ValueError("Card not found")
        if amount > card.balance:
            raise ValueError("Insufficient funds") 
        card.balance -= amount
        self.repository.save_card(card)
        return card.balance



import unittest
from unittest.mock import MagicMock
from models import VirtualCard
from service import VirtualCardService

class TestVirtualCardService(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.service = VirtualCardService(self.mock_repo)
        self.test_card = VirtualCard(card_id="123", user_id="u1", balance=100.0)

    def test_get_balance_success(self):
        self.mock_repo.get_card_by_id.return_value = self.test_card
        balance = self.service.get_balance("123")
        self.assertEqual(balance, 100.0)

    def test_get_balance_card_not_found(self):
        self.mock_repo.get_card_by_id.return_value = None
        with self.assertRaises(ValueError):
            self.service.get_balance("999")

    def test_debit_success(self):
        self.mock_repo.get_card_by_id.return_value = self.test_card
        new_balance = self.service.debit("123", 50.0)
        self.assertEqual(new_balance, 50.0)
        self.mock_repo.save_card.assert_called_once()

    def test_debit_insufficient_funds(self):
        self.mock_repo.get_card_by_id.return_value = self.test_card
        with self.assertRaises(ValueError):
            self.service.debit("123", 200.0)

    def test_debit_card_not_found(self):
        self.mock_repo.get_card_by_id.return_value = None
        with self.assertRaises(ValueError):
            self.service.debit("000", 10.0)

if __name__ == '__main__':
    unittest.main()
