### **Language choice and key design decisions**
I chose to use the python coding language for the below reasons:

- It has strong support for web frameworks (like Django and Flask)
- Easy to integrate with payment gateways (Stripe, PayPal, etc.)
- Has powerful cryptographic and data-handling libraries
- Well-suited for building APIs and microservice

I'm well aware that Java would be the better option as it's great for large-scale financial systems, strong security libraries, multi-threading, mature frameworks like Spring Boot. It's already used by banks and fintech. Golang would've another good option for it's fast, low memory usage, great for building high-performance microservices. With all of this being said  aside from the above mentioned reasons as to why I chose python - it is also the coding language that I am more comfortable in working with.


#### **Key Design Decisions**

#### **1. User Authentication**
- Secure login (OAuth2 or token-based authentication)
- Multi-factor authentication (MFA)

#### **2. Card Generation**
- Unique card number (possibly tokenized)
- CVV + expiration date generation
- Optionally link to an issuing bank or sandboxed wallet

#### **3. Transaction Processing**
- Validate merchant requests
- Check user limits, balances
- Log and authorize/decline transactions

#### **4. Security**
- PCI-DSS compliance (real systems must be)
- Tokenization & encryption (use cryptography, PyCrypto, or Fernet)
- Secure storage (e.g., vault, or using Hashicorp Vault/KMS for secrets)

#### **5. Integration**
- Payment processor (e.g., Stripe Issuing API, Visa/Mastercard APIs)
- Webhooks for real-time transaction updates

#### **6. Admin & User Interfaces**
- Dashboard for users to view virtual cards and usage
- Admin panel for monitoring fraud, logs, etc.
