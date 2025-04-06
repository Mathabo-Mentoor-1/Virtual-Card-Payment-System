
# Activity Diagrams

<br>
## 1. User Registration and Identity Verification

```mermaid
flowchart TD
    %% Define Swimlanes
    subgraph User Registration
        direction TB
        UR_Start[Start] --> UR_EnterDetails[Enter Personal Information]
        UR_EnterDetails --> UR_AccountCreation[Create Account]
        UR_AccountCreation --> UR_EmailVerification[Verify Email]
        UR_EmailVerification --> UR_PasswordSet[Set Password]
        UR_PasswordSet --> UR_Success[Registration Success]
        UR_Success --> UR_End[End]
    end

    subgraph Identity Verification
        direction TB
        IV_Start[Start] --> IV_CollectDocuments[Collect Documents]
        IV_CollectDocuments --> IV_FacialRecognition[Perform Facial Recognition]
        IV_FacialRecognition --> IV_DocumentVerification[Verify Documents]
        IV_DocumentVerification --> IV_Success[Identity Verified]
        IV_Success --> IV_End[End]
    end

    %% Parallel Actions between User Registration and Identity Verification
    UR_AccountCreation --> IV_CollectDocuments
    IV_Success --> UR_Success

    %% Decision Node for User Verification Step
    IV_DocumentVerification -->|Verified| IV_Success
    IV_DocumentVerification -->|Failed| IV_Failed[Verification Failed]
    IV_Failed --> IV_End
    IV_Success --> UR_Success

    %% Join point between User Registration and Identity Verification
    UR_Success --> IV_Start


```
<br>

## 2. Virtual Card Generation and Management

```mermaid
flowchart TD
    %% Define swimlanes for User, System, and Bank
    subgraph User [User]
        direction TB
        UC1[Submit Request for Virtual Card] --> UC2[Provide Payment Information]
    end

    subgraph System [System]
        direction TB
        S1[Verify User Details] --> S2[Generate Virtual Card Details]
        S3[Send Virtual Card Details to User] --> S4[Monitor Transactions]
        S5[Handle Transaction Requests] --> S6[Approve or Decline Transaction]
    end

    subgraph Bank [Bank]
        direction TB
        B1[Receive Transaction Request] --> B2[Process Payment]
        B3[Confirm Payment] --> B4[Update Account Balance]
    end

    %% Actions for the User
    UC1 -->|Submit Card Request| S1
    UC2 -->|Provide Payment Information| S1

    %% Actions for the System
    S1 -->|User Verified| S2
    S2 -->|Virtual Card Created| S3
    S3 --> UC1
    S4 -->|Monitor Active Cards| S5
    S5 -->|Transaction Request Sent| B1
    B1 -->|Transaction Data Sent| B2
    B2 -->|Payment Processing| B3
    B3 -->|Payment Confirmation| S6
    S6 -->|Transaction Approved/Declined| S4

    %% Bank’s actions
    B4 -->|Update User Account| S6

    %% Decision: Validate Card
    S2 -->|Invalid Info| S1
    S6 -->|Transaction Declined| S4
    S6 -->|Transaction Approved| B1

    %% End node
    B4 -->|Transaction Finalized| End[End]

```
<br>

## 3. Payment Authorization and Fraud Detection

```mermaid
flowchart TD
    %% Define Swimlanes
    subgraph A [Customer Actions]
        direction TB
        start_node1([Start])
        choose_card[Customer selects virtual card]
        enter_payment[Enter payment details]
        customer_end([End])
    end

    subgraph B [System Actions]
        direction TB
        verify_card[Verify virtual card]
        check_balance[Check available balance]
        fraud_check[Perform fraud detection]
        authorize_payment[Authorize payment]
        system_end([End])
    end

    subgraph C [Payment Processor Actions]
        direction TB
        send_request[Send payment request]
        receive_response[Receive payment response]
        payment_end([End])
    end

    %% Define start and end nodes
    start_node1 --> choose_card
    choose_card --> enter_payment

    %% System actions
    enter_payment --> verify_card
    verify_card --> check_balance
    check_balance --> fraud_check
    fraud_check --> authorize_payment
    authorize_payment --> send_request

    %% Parallel Actions (Fraud Detection and Authorization)
    fraud_check -->|Check Fraud| authorize_payment
    authorize_payment -->|Proceed to Processor| send_request

    %% Payment Processor Actions
    send_request --> receive_response
    receive_response --> payment_end
    receive_response -->|Success| system_end
    receive_response -->|Failure| fraud_check

    %% Decision Points
    verify_card -->|Invalid| fraud_check
    check_balance -->|Insufficient Funds| fraud_check
    fraud_check -->|Fraud Detected| fraud_check
    fraud_check -->|No Fraud| authorize_payment

    %% Connecting End Nodes
    system_end --> customer_end
    payment_end --> customer_end


```
<br>

## 4. Transaction Logging and Reporting

```mermaid

flowchart TD
    subgraph Cardholder [Cardholder]
        A1[Start Transaction] --> A2[Enter Payment Details]
    end

    subgraph PaymentGateway [Payment Gateway]
        B1[Validate Payment Details] --> B2[Process Payment]
        B2 --> B3{Is Payment Successful?}
    end

    subgraph TransactionLogger [Transaction Logger]
        C1[Log Transaction] --> C2[Check if Logging Error Occurs]
    end

    subgraph ReportingSystem [Reporting System]
        D1[Generate Report] --> D2[Send Report to Admin]
    end

    %% Flow between Swimlanes

    A2 --> B1
    B3 -->|Yes| C1
    B3 -->|No| B4[Notify Cardholder of Failure]
    C2 -->|Error Occurred| C3[Alert Admin]
    C2 -->|No Error| D1
    D1 --> D2
    D2 --> End[End]

    %% Parallel Actions (Transaction Logging and Reporting)
    B1 -->|Log Payment Details| C1
    B1 -->|Generate Real-Time Report| D1

    %% Add start and end nodes
    Start[Start] --> A1
    End[End] --> D2

    %% Decision Nodes
    B3 -->|Is Payment Successful?| C1
    C2 -->|Error Occurred| C3

    %% Styling for Swimlanes (Optional for clarity)
    class Cardholder fill:#f9f,stroke:#333,stroke-width:2px;
    class PaymentGateway fill:#f9f,stroke:#333,stroke-width:2px;
    class TransactionLogger fill:#f9f,stroke:#333,stroke-width:2px;
    class ReportingSystem fill:#f9f,stroke:#333,stroke-width:2px;

```
<br>

## 5. Card Suspension and Deactivation

```mermaid
flowchart TD
    %% Define swimlanes
    subgraph Customer[Customer]
        direction LR
        A[Start] --> B[Request Card Suspension]
    end

    subgraph Bank_System[Bank System]
        direction TB
        B --> C[Verify Card Status]
        C --> D{Is Card Active?}
        D -- Yes --> E[Suspend Card]
        D -- No --> F[Check Deactivation Requirement]
        F --> G{Is Deactivation Required?}
        G -- Yes --> H[Deactivate Card]
        G -- No --> I[Notify Admin]
        E --> J[Notify Customer]
        F --> I
    end

    subgraph Admin[Admin]
        direction LR
        I --> K[Update Internal Systems]
    end

    %% End Node
    K --> L[End]

    %% Parallel Actions
    J -.-> L[End]
    K -.-> L


```
<br>

## 6. Recurring Payment Setup and Management

```mermaid
%%{init: {"themeVariables": {"primaryColor": "#4F9BBF", "edgeLabelBackground":"#FFFFFF", "tertiaryColor": "#FFAD00"}}}%%
flowchart TD
    %% Define Swimlanes
    subgraph User [User]
        direction TB
        A1[Start: User initiates recurring payment setup] --> A2[Enter Payment Info]
        A2 --> A3[Provide Card Details]
        A3 --> A4[Select Recurring Payment Option]
        A4 --> A5[Enter Payment Frequency]
        A5 --> A6[Confirm Recurring Payment Setup]
    end

```

<br>

## 7. Currency Conversion and International Transactions

```mermaid

flowchart TD
    %% Swimlanes
    subgraph A [Customer Interaction]
        A1[Start: Customer Initiates Transaction]
        A2[Select Payment Method]
        A3[Enter Transaction Amount]
        A4[Submit Payment Request]
        A5[End: Transaction Complete]
    end

    subgraph B [Payment System Operations]
        B1[Validate Payment Details]
        B2[Check Currency Conversion Requirement]
        B3[Fetch Conversion Rates]
        B4[Perform Currency Conversion]
        B5[Process Payment Request]
        B6[End Transaction]
    end

    subgraph C [Bank/Payment Gateway]
        C1[Verify Available Funds]
        C2[Check for International Payment Fee]
        C3[Transfer Funds]
    end

    %% Start/End Nodes
    A1 --> A2
    A2 --> A3
    A3 --> A4
    A4 --> B1
    B1 --> B2

    %% Decision Nodes
    B2 -->|Yes| B3
    B2 -->|No| B5

    %% Parallel Actions
    B3 --> B4
    B3 --> C1

    %% Decision on Fund Availability
    C1 -->|Funds Available| C3
    C1 -->|Funds Unavailable| A5

    %% Currency Conversion Process
    B4 --> B5

    %% Payment Process
    B5 --> C2
    C2 -->|Fee Applicable| C3
    C2 -->|No Fee| C3

    C3 --> B6
    B6 --> A5


```
<br>

## 8. Compliance and Regulatory Reporting

```mermaid
flowchart TB
    %% Define Swimlanes
    subgraph System
        direction LR
        A1[Start] --> A2[Check Transaction Data]
        A2 --> A3[Verify Transaction Rules]
        A3 --> A4[Generate Transaction Report]
        A4 --> A5[Send Report to Compliance Team]
    end
    
    subgraph Compliance Team
        direction LR
        B1[Review Transaction Report] --> B2[Approve or Reject]
    end

```