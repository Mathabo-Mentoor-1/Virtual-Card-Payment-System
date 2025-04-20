import copy

class VirtualCardPrototype:
    def __init__(self, card_type, number):
        self.card_type = card_type
        self.number = number

    def clone(self):
        return copy.deepcopy(self)

# Example Usage:
# original = VirtualCardPrototype("Visa", "4111111111111111")
# cloned = original.clone()
