class CardRegistry:
    _instance = None
    _cards = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CardRegistry, cls).__new__(cls)
        return cls._instance

    def register_card(self, alias, card):
        self._cards[alias] = card

    def get_card(self, alias):
        return self._cards.get(alias)
