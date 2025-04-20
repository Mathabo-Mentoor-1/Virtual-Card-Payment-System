class TestAbstractFactory(unittest.TestCase):
    def test_virtual_card_creation(self):
        factory = DebitCardFactory()
        card = factory.create_virtual_card()
        self.assertIsInstance(card, DebitCard)
        self.assertEqual(card.card_holder, "Carol")
