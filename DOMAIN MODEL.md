### Domain Model Description
<br>

| No. | Entity      | Attributes                                                    | Methods                                                      | Relationships                                              |
| --- | ----------- | ------------------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- |
| 1   | User        | user_id, name, email, phone, account_status, created_at       | register(), authenticate(), updateProfile(), deleteAccount() | Owns one or more Accounts and VirtualCards                 |
| 2   | Account     | account_id, user_id, balance, currency, status, created_at    | deposit(), withdraw(), getBalance()                          | Belongs to a User, linked to VirtualCards and Transactions |
| 3   | VirtualCard | card_id, account_id, card_number, cvv, expiry_date, status    | generate(), deactivate(), limitUsage(), getCardDetails()     | Belongs to an Account, used in Transactions, has CardLimit |
| 4   | Transaction | transaction_id, card_id, amount, merchant, timestamp, status  | processPayment(), refund(), getStatus()                      | Linked to a VirtualCard, may be disputed by a User         |
| 5   | CardLimit   | limit_id, card_id, daily_limit, monthly_limit, spending_limit | setLimit(), updateLimit(), enforceLimit()                    | Belongs to a VirtualCard                                   |
| 6   | Merchant    | merchant_id, name, category, location, verified               | verifyMerchant(), getMerchantInfo()                          | Involved in Transactions                                   |
| 7   | AuditLog    | log_id, user_id, action, timestamp, details                   | recordAction(), getLogsByUser(), filterLogs()                | Linked to a User or Transaction, monitors system activity  |


<br>

### Business Rules

#### **1. Security & Fraud Prevention**

1.1 **Card Expiration Limits**:

- Virtual cards must have a default expiration period (e.g., 30 days) unless set by the user.

1.2 **Single/Multi-use Configuration**:

- Cards can be configured as single-use (expires after first transaction) or multi-use (within a specified time or limit).

1.3 **Transaction Authorization**:

- Require 2FA (e.g., SMS, biometric, or app confirmation) before issuing a virtual card.

1.4 **Spending Controls**:

- Set per-transaction and daily/monthly spending limits.
- Restrict merchant categories (MCC codes) if needed.

1.5 **Geo-fencing Rules**:

- Option to allow or block cards based on geographical locations.

1.6 **Card Locking**:

- Users must be able to immediately suspend or delete a virtual card.

<br>

#### 2. **Usage & Transaction Rules**

2.1 **Currency Support**:

- Cards must support multi-currency transactions or be limited to the user's default currency.

2.2 **Refund Handling**:

- Refunds must be credited back to the originating virtual card.
- If card is deleted, funds reroute to user’s primary funding source.

2.3 **Subscription Detection**:

- Notify users if recurring payments are detected.
- Option to block subscription charges by default.

2.4 **Maximum Number of Cards**:

- Users can create a maximum of X virtual cards per day/month (e.g., 10/day).

2.5 **Transaction Failure Protocols**:

- Notify user with reason codes (e.g., insufficient funds, card expired, blocked merchant).
  
<br>

#### 3. **Card Issuance & Management**
3.1 **Funding Source Requirement**:

- Cards can only be issued against verified funding sources (e.g., bank account, wallet, credit line).

3.2 **Auto-Closure Option**:

- Option to auto-close cards after a set time or number of transactions.

3.3 **User-Defined Labels/Tags**:

- Users can tag cards (e.g., "Amazon", "Trial") for organization.

3.4 **Card Reissuance Policy**:

- Rules for reissuing if a virtual card is compromised (e.g., time delay, limits).

<br>

#### 4. **User Access & Roles**
4.1 **Tiered Access for Teams**:

- Admins can issue/manage cards; members can only use.
- Set spend/request approval flows.

4.2 **Audit Trail**:

- Maintain logs for who created/modified/used a virtual card.

4.3 **Card Sharing Restrictions**:

- Cards cannot be shared or used on more than X devices/IPs.

4.4 **KYC/AML Compliance**:

- Virtual card access requires verified identity and passed risk checks.

<br>

#### 5. **Monitoring & Analytics**
5.1 **Real-Time Alerts**:

- Notify users for each transaction, declined attempt, or suspicious activity.

5.2 **Budget Reporting**:

- Provide spend summaries per card, merchant, or timeframe.

5.3 **Merchant Insights**:

- Detect merchant patterns, highlight anomalies.

<br>

#### 6. **Compliance & Regulatory**
6.1 **PCI DSS Compliance**:

- Card data must be encrypted, not stored on the client side.

6.2 **Jurisdictional Limits**:

- Virtual card issuance may be limited by user location or local regulations.

6.3 **Data Retention Policy**:

- Store card transaction data for X years (e.g., 5 years) per financial regulations.

