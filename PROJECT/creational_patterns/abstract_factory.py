class VirtualCardUI:
    def display(self):
        pass

class VirtualCardBackend:
    def validate(self):
        pass

class VisaUI(VirtualCardUI):
    def display(self):
        print("Displaying Visa UI")

class MasterCardUI(VirtualCardUI):
    def display(self):
        print("Displaying MasterCard UI")

class VisaBackend(VirtualCardBackend):
    def validate(self):
        print("Validating Visa card")

class MasterCardBackend(VirtualCardBackend):
    def validate(self):
        print("Validating MasterCard card")

class AbstractCardFactory(ABC):
    @abstractmethod
    def create_ui(self):
        pass

    @abstractmethod
    def create_backend(self):
        pass

class VisaCardFactory(AbstractCardFactory):
    def create_ui(self):
        return VisaUI()

    def create_backend(self):
        return VisaBackend()

class MasterCardFactory(AbstractCardFactory):
    def create_ui(self):
        return MasterCardUI()

    def create_backend(self):
        return MasterCardBackend()
