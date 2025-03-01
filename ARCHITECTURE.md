flowchart TB
    User(User) -->|uses| BankingApp
    BankingApp -->|connects to| BankAPI
    BankingApp -->|authenticates with| AuthenticationService
    BankingApp -->|sends notifications to| NotificationService
    BankAPI -->|interacts with| BankDatabase
    BankAPI -->|interacts with| ThirdPartyPaymentGateway

    classDef user fill:#f96;
    classDef app fill:#bbf,stroke:#000,stroke-width:2px;
    classDef api fill:#f66,stroke:#000,stroke-width:2px;
    classDef service fill:#6c6,stroke:#000,stroke-width:2px;

    class User user;
    class BankingApp app;
    class BankAPI api;
    class AuthenticationService service;
    class NotificationService service;
    class BankDatabase service;
    class ThirdPartyPaymentGateway service;

