class VirtualCard:
    def __init__(self, card_type, number):
        self.card_type = card_type
        self.number = number

    def process_payment(self, amount):
        print(f"Processing {amount} with {self.card_type} card ending in {self.number[-4:]}")

class SimpleCardFactory:
    @staticmethod
    def create_card(card_type):
        if card_type == "Visa":
            return VirtualCard("Visa", "4111111111111111")
        elif card_type == "MasterCard":
            return VirtualCard("MasterCard", "5500000000000004")
        else:
            raise ValueError("Unsupported card type")
