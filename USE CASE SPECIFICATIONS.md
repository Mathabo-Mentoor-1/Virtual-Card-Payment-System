1.
Use Case: Login to Payment Platform

Actor: Customer

Description: This use case describes the process a customer follows to log into a virtual-card payment platform to access their account and manage their virtual cards, transactions, and other account settings.

Preconditions:

- The customer has a registered account on the virtual-card payment platform.
- The customer has access to the internet and a device (e.g., computer, mobile phone, tablet).
- The customer has a valid username/email address and password associated with their account.
- The virtual-card payment platform is operational, and the login page is accessible

Postconditions:

- The customer is successfully logged into their account and can access their dashboard or account homepage.
- The customer can view details of their virtual card(s), transactions, and other account-related information.
- The customer can perform various actions like making payments, checking transaction history, or generating new virtual cards.

Basic Flow:

1. **Customer navigates to the login page**:The customer opens the virtual-card payment platform website or mobile app and is directed to the login screen.
2. **Enter credentials**: The customer enters their registered email/username and password in the respective fields.
3. **Submit credentials**:The customer clicks on the "Login" button to submit the entered credentials.
4. **Authentication**:The system validates the provided credentials by checking them against the stored data in the database.If the credentials are correct, the system generates an authentication token/session for the customer.
5. **Access granted**:The system redirects the customer to their account dashboard or homepage.
6. **Confirmation**:The system displays the customer’s account information (e.g., virtual card details, transaction history, etc.).
7. **End of Flow**: The customer is logged in and can begin using the platform.

Alternative Flows:

 **1. Invalid Credentials**

If the customer enters incorrect credentials (wrong email/username or password), the system will:

- Show an error message stating "Invalid email/username or password."
- The customer is prompted to re-enter the correct credentials.
- The customer can also click on "Forgot password" to initiate a password recovery process.

**2. Account Locked**

- If the customer exceeds the allowed number of failed login attempts (e.g., 3), the system locks the account temporarily for security purposes.
- The customer is presented with a message stating: "Your account has been locked due to multiple failed login attempts."
- The customer is provided with an option to either wait for a period of time (e.g., 30 minutes) for the lock to expire or contact customer support for assistance.

**3. Forgot Password**

- If the customer clicks on "Forgot password", they are prompted to enter their registered email address.
- The system sends a password reset link to the registered email address.
- The customer clicks on the link and is redirected to a page where they can create a new password.
- After the new password is set, the customer can proceed to log in with the updated password.

**4. Two-Factor Authentication (Optional)**

- If the platform requires two-factor authentication (2FA) for additional security:
- After the customer submits the login credentials, the system sends a one-time passcode (OTP) to the customer’s registered mobile number or email.
- The customer enters the OTP on the platform.
- If the OTP is valid, the system grants access to the account.
- If the OTP is invalid or expires, the system will prompt the customer to request a new OTP.

**5. Maintenance or System Down**

- If the virtual-card payment platform is undergoing maintenance or is temporarily unavailable, the system will:
- Display an error message: "The platform is temporarily unavailable. Please try again later."
- The customer is unable to log in and must attempt to log in again once the system is back online.

2.
Use Case: Register virtual card

Actor: Customer

Description:

- The virtual card is a digital representation of a physical or separate payment card that can be used for online electronic transactions. The registration process includes providing necessary details, such as the customer’s personal information and payment preferences, and generating a unique virtual card number.

Preconditions:

- The customer must be registered and authenticated in the virtual-card payment system (via username/password or other authentication mechanisms).
- The customer has access to a valid and active payment method, such as a credit card, debit card, or bank account, to link to the virtual card.
- The customer has a stable internet connection to complete the registration process.

Postconditions:

- A new virtual card is generated and linked to the customer’s account in the system.
- The customer can use the virtual card for online transactions, payments, and other supported use cases.
- The customer receives a confirmation notification or email with the virtual card details.
- The virtual card is added to the customer’s wallet or available within their account for future transactions.

Basic Flow:

- **Customer Login**: The customer logs into their virtual-card payment system account.
- **Initiate Virtual Card Registration**: The customer navigates to the "Virtual Card" section and selects the option to "Create a New Virtual Card."
- **Provide Details**: The system prompts the customer to enter necessary details such as:
- Personal Information (e.g., name, address)
- Linked Payment Method (credit/debit card or bank account)
- Preferences (such as limit, expiration date, etc.)
- **Validation**: The system validates the provided information (e.g., payment method is valid, sufficient funds, etc.).
- **Generate Virtual Card**: If validation is successful, the system generates a new virtual card, complete with a unique card number, expiry date, and CVV.
- **Confirmation**: The system displays the virtual card details on the screen and sends a confirmation email or notification to the customer.
- **End**: The virtual card is successfully created and ready for use.

Alternative Flows:

**1. Invalid Payment Method**

- The customer enters an invalid or expired payment method.
- The system detects the issue and prompts the customer to correct the payment details.
- The customer updates the payment method and continues the registration process from step 4 of the Basic Flow.

**2. Insufficient Funds**

- The customer provides valid payment details, but their payment method has insufficient funds or credit.
- The system detects insufficient funds and prompts the customer to either add funds or use a different payment method.
- The customer resolves the issue and proceeds with registration as in the Basic Flow.

**3. Authentication Failure**

- The customer attempts to log in, but fails to authenticate (e.g., incorrect password).
- The system denies access and provides options for password recovery.
- The customer resets their password and successfully logs in to continue the registration process.

**4. Card Generation Error**

- If there's a system failure or error in generating the virtual card, the system notifies the customer of the issue (e.g., "Unable to create virtual card at the moment").
- The customer can try the registration again or contact customer support for further assistance.

3.
Use Case: Make payment

Actor: Customer,Merchant & Payment Gateway

Description: A customer makes a payment for services using a virtual card. The system processes the payment, deducting the correct amount from the virtual card balance and completing the transaction.

Preconditions:

- **Customer Account**: The customer must have an active account in the virtual card payment system.
- **Virtual Card**: The customer must have a valid virtual card with sufficient funds or credit to cover the purchase.
- **Payment Gateway Access**: The system must be connected to a payment gateway for the transaction to be processed.
- **Merchant Acceptance**: The merchant must accept payments via virtual cards.

Postconditions:

- **Payment Successful**: The transaction is successfully completed, and the amount is deducted from the virtual card balance.
- **Transaction Record**: A payment transaction record is created, detailing the transaction date, merchant, amount, and transaction ID.
- **Notification**: The customer receives a confirmation of the payment (via email, SMS, or app notification).
- **Merchant Receives Funds**: The merchant receives the agreed amount, minus any processing fees, as per the agreement with the payment provider.

Basic Flow:

**Customer Initiates Payment**:

- The customer selects the virtual card as the payment method at checkout.
- The virtual card details (card number, expiration date, and CVV) are either auto-filled or entered manually by the customer.

**System Verifies Virtual Card**:

- The virtual card information is sent to the payment gateway for validation.
- The payment gateway verifies that the card is valid, active, and has sufficient funds or credit for the transaction.

**Authorization**:

- The payment gateway sends a request to the virtual card issuer to authorize the payment.
- The issuer checks the balance and approves or declines the transaction.

**Transaction Confirmation**:

- If approved, the payment gateway confirms the transaction and processes the payment, deducting the amount from the virtual card’s balance.

**Notification and Receipt**:

- The customer receives a confirmation of the transaction (email, SMS, or app notification).
- The customer is shown the payment receipt, which includes transaction details (merchant, amount, date).

**Merchant Notification**:

- The merchant is notified of the successful payment.
- The merchant’s account is credited with the payment, minus any fees.

Alternative Flows:

**1. Insufficient Funds or Credit**

- **Step**: The payment system detects insufficient funds or credit.
- **Alternative Flow**:
  - The payment is declined.
  - The customer is notified of the insufficient funds or credit.
  - The customer may choose to enter another payment method or add funds to the virtual card.

**2. Invalid Card Information**

- **Step**: The system detects invalid or expired card details.
- **Alternative Flow**:
  - The payment is declined.
  - The customer is prompted to verify and update their card details.

**3. Payment Gateway Error**

- **Step**: The payment gateway encounters an issue (e.g., network failure, server error).
- **Alternative Flow**:
  - The payment attempt is not completed.
  - The customer is notified of the error and asked to try again or use another payment method.

**4. Merchant Declines Payment**

- **Step**: The merchant rejects the payment for reasons like fraud detection or unavailable goods.
- **Alternative Flow**:
  - The transaction is canceled, and the customer is notified that the merchant declined the payment.
  - The customer may contact the merchant for more details or choose another item to purchase.

4.
Use Case: Check payment status

Actor: Customer,Merchant & Payment Gateway

Description:

This use case describes the process in which a customer checks the payment status for a transaction made using their virtual card in a virtual-card payment system. The customer can verify whether a payment has been successfully processed, is pending, or has failed, through a customer-facing interface (e.g., mobile app, website).

Preconditions:

- The customer has an active virtual card issued by the system.
- The customer has made at least one payment using the virtual card.
- The customer is authenticated and logged into their account (either via website or mobile app).
- The payment system must be operational, and the relevant payment gateway should have been notified of the payment

Postconditions:

- **Successful Outcome:** The customer is presented with the current payment status of the specific transaction, which could be:

1. Success: Payment was processed successfully.
2. Pending: Payment is awaiting confirmation or processing.
3. Failed: Payment was unsuccessful due to some issue (e.g., insufficient funds, payment gateway error).

- **Failed Outcome:** If the customer encounters issues (e.g., payment not found), they should be provided with a relevant error message and potential next steps (e.g., contact support, retry payment, etc.).

Basic Flow:

**Customer Logs In:**

- The customer accesses the system (either mobile app or website).
- The customer enters login credentials (username/password) or uses an alternate login method (e.g., two-factor authentication).

**Navigate to Payment History:**

- The customer navigates to the payment history or transaction section of the app/website.
- A list of past transactions is displayed, including the payment amounts, dates, and transaction status (if available).

**Select a Specific Transaction:**

- The customer selects the specific transaction they wish to check from the list.
- The system fetches detailed information regarding the payment status, including transaction ID, payment amount, date, and current status (success, pending, or failed).
- **View Payment Status:**The system displays the payment status along with any relevant details (e.g., a success message, pending status with expected time for completion, or a failed status with a reason code).
- **End Process:**The customer can either choose to check another payment, go back to the dashboard, or log out.

Alternative Flows:

**No Transaction Found:**

1. If the customer selects a transaction that doesn’t exist or the transaction is not found in the system (e.g., due to a technical issue or data discrepancy), the system displays an error message: "Transaction not found."
2. The system may prompt the customer to retry or contact customer support.
3. The customer either chooses to retry or exits the payment history section.

**System Error or Payment Gateway Issue:**

1. If there is a problem with the payment gateway (e.g., failure to retrieve the payment status), the system displays a message like "Error fetching payment status."
2. The system provides the option to retry or notify the customer that support should be contacted.
3. The customer may retry the operation after a few minutes or contact support for further assistance.

**Pending Payment Status:**

- If the payment status is marked as "Pending," the system will show additional details such as expected time for processing or a message indicating that the payment is under review or awaiting confirmation.
- The customer can choose to wait or contact support for more information about the delay.

**Failed Payment:**

- If the payment status is "Failed," the system provides the failure reason (e.g., "Insufficient funds," "Payment gateway issue," etc.).
- The customer can attempt to reprocess the payment, or the system may offer instructions on resolving the issue (e.g., update payment information, ensure sufficient funds).

5.
Use Case: Notify user of payment

Actor: Notification Service

Description:

- The Payment Notification Service is responsible for notifying users about the status of their virtual card payments. This notification system will alert users via email, SMS, or app notification when a payment is made successfully, fails, or encounters an issue.

Preconditions:

- The Payment Notification Service is responsible for notifying users about the status of their virtual card payments. This notification system will alert users via email, SMS, or app notification when a payment is made successfully, fails, or encounters an issue.

Postconditions:

- The user receives an appropriate notification about the payment status (successful, failed, or pending).
- The payment notification is logged for auditing purposes.
- The system ensures delivery of the notification (e.g., retries in case of failure).

Basic Flow:

**Step 1: Payment Initiation**

- The user initiates a payment through their virtual card (e.g., purchasing a product or service).

**Step 2: Payment Processing**

- The system processes the payment, checking for sufficient funds, card validity, etc.

**Step 3: Notification Trigger**

- Once the payment is completed (either successful, failed, or pending), the system triggers a notification to the user.

**Step 4: Notification Delivery**

- The notification service sends a notification to the user through the configured channels (email, SMS, or app).
- The content of the notification includes the payment status (success, failure, or pending), amount, and any necessary details (error message if the payment fails, or confirmation if the payment succeeds).

**Step 5: User Receives Notification**

- The user receives the notification on their chosen communication platform (email, SMS, or app).

Alternative Flows:

**Payment Failure**

- **Step 1:** The user attempts to make a payment, but the payment fails due to issues like insufficient funds or card expiry.
- **Step 2:** The system processes the failure.
- **Step 3:** The system triggers a notification about the failure and the reason (e.g., "Insufficient funds" or "Card expired").
- **Step 4:** The user receives the notification informing them of the failure.

**Notification Delivery Failure**

- **Step 1:** The payment is successfully processed, but the notification fails to be delivered (e.g., email server down, SMS service unavailable).
- **Step 2:** The system logs the notification failure and retries sending the message after a predefined period (e.g., 10 minutes).
- **Step 3:** The user is eventually notified successfully or is alerted with an alternative method if the retry fails.

**User Not Registered for Notifications**

- **Step 1:** The system tries to send a payment notification but detects the user hasn't opted for notifications (no email or SMS configured).
- **Step 2:** The system can send a default in-app notification or prompt the user to configure their notification settings in the future.

6.

Use Case: Send payment of notification

Actor: Notification Service

Description:

- The Notification Service in a virtual-card payment system is responsible for sending notifications (such as payment confirmation, payment failure, or payment status updates) to users after a transaction has been completed. These notifications ensure that users are informed about the status of their payments, whether successful or failed, and provide additional information as needed.

Preconditions:

- The user has successfully made a payment using the virtual card system.
- The payment transaction has been processed and verified by the payment gateway or processor.
- The user has registered their contact details (email, SMS, or app notifications) for receiving notifications.
- The notification service is operational and ready to send notifications.
- The transaction status (success or failure) is available.

Postconditions:

- The user receives a notification with the details of the payment status.
- The system logs the notification event for future audit or troubleshooting.
- If applicable, the user is informed of any necessary follow-up actions (e.g., retrying a failed payment).

Basic Flow:

**Step 1: User initiates a payment**

- The user makes a payment using the virtual card.

**Step 2: Payment Processing**

- The payment is processed by the payment gateway.
- The system receives confirmation of payment status (success or failure).

**Step 3: Notification Preparation**

- Based on the payment status, the notification service prepares the appropriate notification. For example:
  - "Payment Successful: Your payment of R100 has been successfully processed."
  - "Payment Failed: Your payment of R100 could not be processed due to insufficient funds."

**Step 4: Sending Notification**

- The notification is sent to the user's registered communication channel (email, SMS, push notification, etc.).

**Step 5: Log Event**

- The notification event is logged for future reference (e.g., for debugging or customer support).

Alternative Flows:

**Step 1: User initiates a payment**

- The user initiates a payment using the virtual card.

**Step 2: Payment Processing**

- The payment is processed by the payment gateway, but an issue occurs (e.g., insufficient funds, payment declined).

**Step 3: Payment Failure**

- The system detects the failure and triggers a notification preparation process.

**Step 4: Notification Preparation**

- The notification service prepares a failure notification (e.g., "Payment Failed: Your payment of R100 could not be processed. Please check your account balance or try again").

**Step 5: Retry Attempt**

- The system may provide an option to retry the payment or provide instructions on how to resolve the issue (e.g., "Please contact your bank").

· **Step 6: Sending Failure Notification**

- The failure notification is sent to the user via the registered communication channel.

**Step 7: Log Event**

- The failure event is logged for auditing purposes and troubleshooting.

7.
Use Case: Add funds to card

Actor: Bank

Description:

- The "Add Funds to Card" process allows a user to deposit money into their virtual card to facilitate online transactions. The funds can be added from various payment sources, including bank accounts, linked wallets, or other pre-defined funding sources.

Preconditions:

- The user must have an active account with the bank or payment provider.
- The user must have an active virtual card linked to their account.
- The user must have sufficient funds in their linked account or funding source.
- The user must be authenticated and logged into the system.
- The virtual card should not be restricted or frozen (it should be in good standing).

Postconditions:

- The requested funds are successfully transferred to the virtual card.
- The balance of the virtual card is updated and reflected in real time.
- A confirmation notification is sent to the user, detailing the amount added and the updated balance.
- The transaction history of the virtual card is updated to reflect the addition of funds.

Basic Flow:

**User Authentication:**

- The user logs into their account using their credentials (e.g., username and password, two-factor authentication).

**Navigate to Add Funds Section:**

- After logging in, the user selects the "Add Funds" or "Top Up" option from the virtual card menu.

**Choose Funding Source:**

- The system displays a list of available funding sources (e.g., bank account, linked wallet, debit/credit card).

**Enter Amount:**

- The user enters the amount they wish to add to the virtual card.

**Confirm Payment:**

- The user is prompted to confirm the amount and the selected funding source.
- If necessary, the user enters payment details for the funding source (e.g., account number or card details).

**Verification & Processing:**

- The system verifies the user's funds and payment source.
- If everything is in order, the system processes the transaction and adds the funds to the virtual card.

**Confirmation:**

- A confirmation message is displayed, showing the added amount and the updated virtual card balance.
- The system updates the transaction history for the virtual card.

**User Receives Confirmation:**

- The user receives a confirmation notification (email, SMS, or in-app notification) detailing the amount added and updated card balance.

Alternative Flows:

**Insufficient Funds in Source Account:**

- If the user’s bank account or funding source has insufficient funds, the system displays an error message.
- The user is prompted to select a different funding source or add funds to the current account and try again.

**Invalid or Expired Payment Details:**

- If the user enters invalid or expired payment details (e.g., expired credit card), the system alerts the user and prompts them to update their details.
- The user can then retry the transaction with updated information.

**Transaction Limit Exceeded:**

- If the user tries to add funds beyond the allowed limit for the virtual card, the system will display an error message.
- The user can choose a smaller amount to proceed.

**User Cancels Transaction:**

- During any step of the process, the user can cancel the fund-adding process. The system returns to the previous screen or home page without making any changes.

**Payment Gateway Error:**

- If the payment gateway encounters an issue (e.g., network failure, downtime), the system will notify the user of the failure and offer the option to retry the transaction later.

8.

Use Case: Verify payment security

Actor: Bank & Fraud Detection System

Description:

- The payment security for the virtual-card payment system focuses on ensuring that all transactions are authorized and monitored to prevent fraud. It involves encryption, authentication, and fraud detection algorithms to protect both the cardholder and the bank.
- **Encryption**: All data transmitted during the transaction, including card details and personal information, must be encrypted using secure protocols like SSL/TLS to prevent eavesdropping and tampering.
- **Tokenization**: Real card details are replaced with a token (a unique identifier) during the transaction to further secure sensitive information.
- **Authentication**: Multi-factor authentication (MFA) or biometric authentication (such as fingerprint or facial recognition) is used to verify the identity of the cardholder.
- **Fraud Detection Algorithms**: Machine learning or rule-based systems monitor for suspicious patterns in transactions, such as unusual locations or amounts, and trigger alerts for further review.

Preconditions:

These are the conditions that must be true before the transaction can proceed.

- **Valid Virtual Card**: The user must have a valid virtual card that is linked to their bank account or virtual wallet.
- **Sufficient Funds**: The account must have enough funds for the transaction.
- **Authentication Verified**: The user must have passed multi-factor authentication or any required identity verification steps.
- **System Availability**: The fraud detection and payment system should be operational, ensuring that there are no service outages.
- **Virtual Card Enabled for Transactions**: The virtual card must be enabled for online or virtual transactions.

Postconditions:

These conditions must be true after the transaction has been completed.

- **Transaction Approved**: The payment has been successfully processed, and funds are transferred to the merchant or recipient.
- **Transaction Logged**: The transaction details, including time, amount, user, and merchant, are securely logged in the bank’s system for auditing and future reference.
- **Fraud Detection Triggered (if applicable)**: If suspicious behavior is detected, the transaction is flagged for review, and the cardholder may be notified to verify or dispute the transaction.
- **Account Updated**: The virtual card balance or linked bank account is updated accordingly, reflecting the payment amount or transaction.
- **Virtual Card Status (if applicable)**: If the transaction is flagged as fraudulent, the virtual card may be deactivated, and the user may be asked to report the fraud.

Basic Flow:

The basic flow outlines the primary sequence of events for a successful transaction.

- **User Initiates Payment**: The user enters the payment details on the merchant’s website or app.
- **Payment Information Transmitted**: The virtual card information (token) is transmitted to the payment gateway.
- **Bank Verification**: The bank checks if the virtual card is valid and has sufficient funds. It also verifies the user's identity through multi-factor authentication.
- **Fraud Detection**: The fraud detection system analyzes the transaction for any irregularities, such as unusual locations, spending patterns, or device fingerprinting anomalies.
- **Transaction Authorization**: If the payment passes the fraud detection checks, the bank authorizes the transaction.
- **Merchant Confirmation**: The merchant receives the payment confirmation and the transaction is completed.
- **Logging**: The system logs the transaction, including relevant details for future reference.

Alternative Flows:

The alternative flows cover scenarios where the basic flow is interrupted or where certain conditions are not met.

**1: Insufficient Funds**

- If the account linked to the virtual card does not have sufficient funds, the transaction is declined.
- The user is notified of the insufficient funds and can choose to cancel the transaction or use another payment method.

**2: Fraud Detection Alert**

- If the fraud detection system detects suspicious activity (e.g., unusual location, large amount, or rapid consecutive transactions), it triggers an alert.
- The user is prompted to confirm the transaction via a secure communication channel (e.g., email, SMS, or app notification).
- If the user confirms the transaction, it proceeds; otherwise, the transaction is flagged, and the virtual card may be deactivated until further investigation.

**3: Failed Authentication**

- If the user fails to pass multi-factor authentication (e.g., wrong password or fingerprint), the transaction is rejected.
- The user is asked to retry authentication or provide additional verification (e.g., using a backup authentication method like email verification).

**4: System Timeout or Error**

- If there is a system failure or timeout during the transaction processing (e.g., communication failure between the bank and the merchant), the transaction may be temporarily held or canceled.
- The user is notified of the error and may be prompted to try the transaction again later.

**5: Virtual Card Deactivated**

- If the virtual card is reported as stolen or compromised, it will be deactivated, preventing any further transactions.
- The user is notified of the deactivation, and they may request a replacement virtual card.
