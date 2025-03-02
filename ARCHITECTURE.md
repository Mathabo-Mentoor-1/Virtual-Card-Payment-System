
graph TD
    A[User] -->|Uses| B[Banking App]
    B -->|Requests Transfer| C[Banking Server]
    C -->|Checks Account Balance| D[User Bank Account]
    C -->|Requests Transfer Authorization| E[External Payment Gateway]
    E -->|Authorizes Payment| F[External Bank Account]
    F -->|Transfer Confirmation| C
    C -->|Confirms Transfer| A
    B -->|Displays Transfer Status| A
