import unittest

class TestSimpleFactory(unittest.TestCase):
    def test_credit_card_creation(self):
        card = SimpleCardFactory.create_card('credit', '1234', 'Alice', 1000)
        self.assertIsInstance(card, CreditCard)
        self.assertEqual(card.card_holder, 'Alice')
        self.assertEqual(card.balance, 1000)

    def test_invalid_card_type(self):
        with self.assertRaises(ValueError):
            SimpleCardFactory.create_card('gift', '0000', 'Bob', 0)
