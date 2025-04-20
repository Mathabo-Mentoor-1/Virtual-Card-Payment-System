class TestBuilder(unittest.TestCase):
    def test_card_building(self):
        builder = CardBuilder()
        card = (builder.set_card_number("9999")
                      .set_card_holder("Dave")
                      .set_balance(500)
                      .build())
        self.assertIsInstance(card, VirtualCard)
        self.assertEqual(card.card_holder, "Dave")
        self.assertEqual(card.balance, 500)
