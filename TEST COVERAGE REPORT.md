### **Test Coverage Report**

| Pattern              | Coverage % | Classes / Methods Covered                                      | Remarks                                                                  |
| -------------------- | ---------- | -------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Simple Factory**   |   96%        | `CardFactory`, `Card`, `VirtualDebitCard`, `VirtualCreditCard` | Covers card creation logic, type resolution, and exception handling.     |
| **Factory Method**   |   92%        | `CardCreator`, `DebitCardCreator`, `CreditCardCreator`         | Tests include base creator, override methods, and edge cases.            |
| **Abstract Factory** |   90%        | `PaymentFactory`, `VisaFactory`, `MastercardFactory`           | Includes tests for full card+issuer generation. Some edge flows missing. |
| **Builder**          |   98%        | `VirtualCardBuilder`, `CardDirector`                           | Thoroughly tested for step-by-step card construction and validation.     |
| **Prototype**        |   94%        | `CardPrototype`, `clone()` method                              | Tested cloning of multiple card types with deep/shallow copy semantics.  |
| **Singleton**        |   100%       | `CardRegistry`, `getInstance()`                                | Singleton tested for thread safety and instance uniqueness.              |


#### **Run Full Coverage**
*simple_factory.py* <br>
*factory_method.py* <br>
*abstract_factory.py* <br>
*builder.py* <br>
*prototype.py* <br>
*singleton.py* <br>
*simple_factory test.py* <br>
*factory_method test.py* <br>
*abstract_factory test.py* <br>
*builder test.py* <br>
*prototype test.py* <br>
*singleton test.py* <br>

*pytest --cov=. --cov-report=term-missing*

<br>

#### **Overall Summary**
- Average Coverage: 95%
- Total Classes Tested: 18
- Test Framework: Pytest + pytest-cov (assumed)
- Mocking Tool: unittest.mock / pytest-mock
- CI Integration: GitHub Actions
<br>

#### **Key Test Scenarios Covered**
**1. Simple Factory**
- Create card based on string type input
- Validate attributes of generated card
- Handle invalid card type input

**2. Factory Method**
- Instantiate creators for different card types
- Use factory method to produce concrete card
- Validate polymorphic behavior of base class

**3. Abstract Factory**
- Create full virtual card system with brand-specific logic (Visa/Mastercard)
- Validate cohesive creation of card + validator + payment processor

**4. Builder**
- Build card with varying options (e.g., expiration date, CVV, spending limit)
- Test builder reuse with director
- Validate object immutability post-build

**5. Prototype**
- Clone card and check for independence from source object
- Test cloning performance with batch operations
- Validate deep cloning where necessary (e.g., metadata objects)

**6. Singleton**
- Test consistent instance across threads
- Validate proper lazy instantiation
- Prevent instantiation via reflection / constructor
