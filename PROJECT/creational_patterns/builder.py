class VirtualCardBuilder:
    def __init__(self):
        self.card = VirtualCard(None, None)

    def set_type(self, card_type):
        self.card.card_type = card_type
        return self

    def set_number(self, number):
        self.card.number = number
        return self

    def build(self):
        return self.card

# Example Usage:
# builder = VirtualCardBuilder()
# card = builder.set_type("Visa").set_number("4111111111111111").build()
