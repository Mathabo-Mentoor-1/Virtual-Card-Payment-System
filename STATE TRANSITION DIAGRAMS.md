# State Transition Diagrams
<br>

### 1. Virtal Card Number
__________________________________________________________________________________________________________________________

```mermaid
stateDiagram-v2
    [*] --> CardRequested : Request Card
    CardRequested --> CardGenerated : Card Generation Success
    CardRequested --> CardRequestFailed : Card Generation Failed
    CardGenerated --> CardActive : Card Activated
    CardGenerated --> CardGenerationFailed : Card Activation Failed
    CardActive --> TransactionInitiated : Initiate Payment
    CardActive --> CardSuspended : Card Suspended
    CardActive --> CardExpired : Card Expired
    TransactionInitiated --> TransactionApproved : Payment Approved
    TransactionInitiated --> TransactionDenied : Payment Denied
    TransactionApproved --> CardUsed : Card Used
    TransactionDenied --> CardSuspended : Suspect Fraud Detected
    CardSuspended --> CardReactivated : Reactivate Card
    CardSuspended --> CardCancelled : Cancel Card
    CardExpired --> CardCancelled : Cancel Card
    CardUsed --> [*] : End Process
    CardCancelled --> [*] : End Process

```
<br>

### 2. Authentication Token
_____________________________________________________________________________________________________________________________________
```mermaid
stateDiagram-v2
    [*] --> Request : Request Token
    Request --> TokenIssued : Token Generation Success
    TokenIssued --> Verified : Token Verification Success
    TokenIssued --> Expired : Token Expired
    TokenIssued --> Revoked : Token Revoked
    Verified --> [*] : Transaction Complete
    Expired --> [*] : Token Expired
    Revoked --> [*] : Token Revoked

    TokenIssued: Token Valid
    TokenIssued: Token Invalid
    Verified: Token Verified
    Verified: Token Invalid
    Expired: Token Expired
    Revoked: Token Revoked


```
<br>

## 3. Transaction Authorization Code
```mermaid

stateDiagram-v2
    [*] --> Idle

    Idle --> RequestSent : Request transaction
    RequestSent --> Pending : Transaction request received
    Pending --> Validating : Validate transaction details
    Validating --> Approved : Transaction details valid
    Validating --> Rejected : Invalid details or card info
    Approved --> GeneratingTAC : Generate Transaction Authorization Code
    Rejected --> [*] : End transaction (Rejected)
    
    GeneratingTAC --> SentTAC : Send TAC to user
    SentTAC --> Completed : TAC successfully sent
    SentTAC --> Failed : TAC sending failed
    
    Completed --> [*] : End transaction (Completed)
    Failed --> [*] : End transaction (Failed)


```
<br>

## 4. Payment Gateway

```mermaid
stateDiagram-v2
    [*] --> Idle

    Idle --> Processing : Payment Initiated
    Processing --> Success : Payment Approved
    Processing --> Failure : Payment Declined
    Processing --> Error : Payment Error

    Success --> [*] : End Transaction
    Failure --> [*] : End Transaction
    Error --> [*] : End Transaction

    Success --> RefundPending : Refund Requested
    Failure --> RefundPending : Refund Requested
    RefundPending --> Refunded : Refund Processed
    RefundPending --> Error : Refund Failed

    Refunded --> [*] : End Transaction

    Error --> Retry : Retry Requested
    Retry --> Processing : Retry Payment
    Retry --> Error : Retry Failed


```

<br>

## 5. Merchant Account

```mermaid
stateDiagram-v2
    [*] --> Pending
    Pending --> Active: Account validated
    Pending --> Rejected: Validation failed
    Active --> Processing: Transaction initiated
    Active --> Suspended: Account flagged for suspicious activity
    Suspended --> Active: Review passed
    Suspended --> Rejected: Fraudulent activity detected
    Active --> Closed: Account deactivated by merchant
    Closed --> [*]

    Processing --> Completed: Payment authorized
    Processing --> Failed: Payment authorization failed
    Failed --> Pending: Retry transaction
    Failed --> Closed: Merchant cancels account
    Completed --> [*]
    
```

## 6. Security Protocols

```mermaid
stateDiagram-v2
    [*] --> CardEntry
    CardEntry --> Tokenization : Card Data Entered
    Tokenization --> TokenGenerated : Tokenization Successful
    TokenGenerated --> Encryption : Token Ready for Encryption
    Encryption --> EncryptedData : Encryption Successful
    EncryptedData --> PaymentProcessing : Payment Data Ready
    PaymentProcessing --> PaymentAuthorized : Authorization Success
    PaymentAuthorized --> PaymentDeclined : Authorization Failure
    PaymentAuthorized --> [*] : Payment Completed

```
<br>

## 7. Transaction History/Logs
<br>
```mermaid
stateDiagram-v2
    [*] --> Idle

    Idle --> TransactionRequested : RequestTransaction
    TransactionRequested --> Processing : ValidateCardDetails
    Processing --> TransactionCompleted : TransactionApproved
    Processing --> TransactionFailed : TransactionDeclined
    TransactionCompleted --> Logging : LogTransaction
    TransactionFailed --> Logging : LogTransaction
    Logging --> Idle : TransactionLogged

    state TransactionRequested {
        [*] --> CardValidation
        CardValidation --> Pending : CardDetailsValidated
        CardValidation --> Failed : InvalidCardDetails
        Pending --> Processing : PaymentInitiated
        Failed --> Idle : RetryTransaction
    }

    state Processing {
        [*] --> TransactionInProgress
        TransactionInProgress --> Completed : PaymentSuccessful
        TransactionInProgress --> Failed : PaymentFailed
        Completed --> Logging
        Failed --> Logging
    }

    state Logging {
        [*] --> LogEntryCreated
        LogEntryCreated --> [*] : EndLogging
    }

    state TransactionCompleted {
        [*] --> AwaitingConfirmation
        AwaitingConfirmation --> Idle : ConfirmTransaction
    }

    state TransactionFailed {
        [*] --> RetryOrCancel
        RetryOrCancel --> TransactionRequested : RetryTransaction
        RetryOrCancel --> Idle : CancelTransaction
    }

    TransactionRequested -->|CardValid == true| Processing
    TransactionRequested -->|CardValid == false| Failed

    Processing -->|PaymentApproved == true |TransactionCompleted
    Processing -->|PaymentApproved == false |TransactionFailed

    Logging -->|TransactionLogged == true |Idle


```
<br>


## 8. Virtual Account

```mermaid
stateDiagram-v2
    [*] --> Idle : Start

    state Idle {
        [*] --> WaitingForPaymentDetails
        WaitingForPaymentDetails --> VerifyingPaymentDetails : PaymentDetailsEntered
        VerifyingPaymentDetails --> PaymentValidated : ValidPaymentDetails
        VerifyingPaymentDetails --> InvalidPaymentDetails : InvalidDetails
        InvalidPaymentDetails --> WaitingForPaymentDetails : RetryPaymentDetails
    }

    state PaymentValidated {
        [*] --> PaymentProcessing
        PaymentProcessing --> PaymentSuccessful : PaymentApproved
        PaymentProcessing --> PaymentFailed : PaymentDeclined
        PaymentFailed --> PaymentProcessing : RetryPayment
    }

    state PaymentSuccessful {
        [*] --> AccountDebited
        AccountDebited --> [*] : TransactionComplete
    }

    state PaymentFailed {
        [*] --> AccountReverted
        AccountReverted --> [*] : TransactionFailed
    }

    state AccountDebited {
        [*] --> TransactionComplete
        TransactionComplete --> [*] : EndTransaction
    }

    WaitingForPaymentDetails --> InsufficientFunds : CheckBalance < 0
    InsufficientFunds --> WaitingForPaymentDetails : DepositFunds
    AccountDebited --> SuccessfulTransaction : BalanceSufficient
    InsufficientFunds --> PaymentFailed : TransactionDeclined


```