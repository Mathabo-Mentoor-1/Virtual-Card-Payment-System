class TestPrototype(unittest.TestCase):
    def test_card_cloning(self):
        original = CardPrototype("5555", "Eve", 700)
        clone = original.clone()
        self.assertIsInstance(clone, CardPrototype)
        self.assertEqual(clone.card_number, original.card_number)
        self.assertIsNot(clone, original)  # Different instance
