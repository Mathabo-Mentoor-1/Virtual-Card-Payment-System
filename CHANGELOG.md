### **Changes after unit testing:**


**1. Bug Fixes**
- Incorrect validation logic (e.g. expiry dates, CVV formats).
- Improper error handling in scenarios like insufficient balance or network failure.
- Faulty calculations in transaction amounts (e.g., currency conversion, fees).
- State management issues, such as a card not being marked inactive after expiration.
<br>

**2. Code Refactoring**
- Breaking down large methods into smaller, reusable ones.
- Removing redundant code or repeated logic.
- Improving naming conventions for readability.
- Applying design patterns (e.g. Strategy, Factory) for modular design.
<br>

**3. Enhanced Security Checks**
- Sanitize and validate all inputs to prevent injection attacks.
-  Ensure tokenization and encryption routines are working as intended.
- Add or improve logging and monitoring for suspicious activities.
- Limit retry attempts for failed transactions (to prevent brute force).
<br>

**4. Edge Case Handling**
- Handling unexpected or malformed inputs gracefully.
- Adding fallback mechanisms for network/API failure scenarios.
- Ensuring system behavior is consistent with high transaction volume.
- Time zone edge cases affecting expiry or transaction times.
<br>

**5. Improved Test Coverage and Automation**
- Writing additional unit tests for uncovered code paths.
- Isolating external dependencies using mocks or stubs (e.g. payment gateways, banking APIs).
- Integrating with CI/CD pipelines to automatically test each code push.
<br>

 **6. Business Logic Updates**
- Modifying the card lifecycle management (e.g. when to activate/deactivate).
- Adjusting limits on usage, daily transactions, or merchant categories.
- Ensuring compliance with regulatory requirements like PCI-DSS or GDPR.
<br>

**7. Improved Logging and Monitoring**
- Add structured logging for key operations (like card creation or payment authorization).
- Implement better exception tracking and alerts.
<br>

**8. Interface Contract Adjustments**
- Update request/response schemas (e.g. include more detailed status messages).
- Ensure backward compatibility or document breaking changes.
- Improve API documentation and versioning.
