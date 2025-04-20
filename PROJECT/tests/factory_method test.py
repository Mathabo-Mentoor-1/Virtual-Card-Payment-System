class TestFactoryMethod(unittest.TestCase):
    def test_factory_method_creates_credit_card(self):
        factory = CreditCardFactory()
        card = factory.create_card()
        self.assertIsInstance(card, CreditCard)
        self.assertEqual(card.card_holder, "Bob")
