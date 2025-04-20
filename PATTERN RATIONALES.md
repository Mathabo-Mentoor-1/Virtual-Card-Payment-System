### **Justification Table: Creational Patterns in a Virtual-Card Payment System**
<br>

| No. | Pattern          | When to Use                                                                                        | Implementation Task Example                                                                                                 |
| --- | ---------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 1   | Simple Factory   | When you need to create objects without exposing the instantiation logic to the client.            | Creating different types of virtual cards (e.g., DebitCard, CreditCard, PrepaidCard) based on user selection.               |
| 2   | Factory Method   | When a class defers the instantiation of objects to its subclasses.                                | A CardIssuer base class defines a method createCard(), subclasses like VisaIssuer, MastercardIssuer override it.            |
| 3   | Abstract Factory | When you need to create families of related or dependent objects without specifying their classes. | Producing a complete set of related objects like VirtualCard, CardValidator, and TransactionHandler for each card provider. |
| 4   | Builder          | When the creation process is complex and should be separated from its representation.              | Building a virtual card with optional features like spending limits, expiration date, and currency preferences.             |
| 5   | Prototype        | When the cost of creating a new object is expensive and cloning is more efficient.                 | Cloning a virtual card configuration for a new user account based on an existing card template.                             |
| 6   | Singleton        | When exactly one instance of a class is needed and it must be globally accessible.                 | Managing the virtual card payment gateway instance that handles all transaction requests.                                   |
