# Simple Factory
visa_card = SimpleCardFactory.create_card("Visa")
visa_card.process_payment(100)

# Factory Method
creator = MasterCardCreator()
card = creator.create_card()
card.process_payment(50)

# Abstract Factory
factory = VisaCardFactory()
ui = factory.create_ui()
backend = factory.create_backend()
ui.display()
backend.validate()

# Builder
builder = VirtualCardBuilder()
custom_card = builder.set_type("Custom").set_number("1234567812345678").build()
custom_card.process_payment(200)

# Prototype
proto_card = VirtualCardPrototype("Visa", "4111111111111111")
cloned_card = proto_card.clone()
print(f"Cloned card: {cloned_card.card_type}, {cloned_card.number}")

# Singleton
registry = CardRegistry()
registry.register_card("main", visa_card)
print(registry.get_card("main").card_type)
