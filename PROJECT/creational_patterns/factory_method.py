from abc import ABC, abstractmethod

class CardCreator(ABC):
    @abstractmethod
    def create_card(self):
        pass

class VisaCardCreator(CardCreator):
    def create_card(self):
        return VirtualCard("Visa", "4111111111111111")

class MasterCardCreator(CardCreator):
    def create_card(self):
        return VirtualCard("MasterCard", "5500000000000004")
