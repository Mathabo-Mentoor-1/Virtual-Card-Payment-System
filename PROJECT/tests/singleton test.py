class TestSingleton(unittest.TestCase):
    def test_singleton_instance(self):
        config1 = CardSystemConfig()
        config2 = CardSystemConfig()
        self.assertIs(config1, config2)
        self.assertEqual(config1.default_balance, 1000)
