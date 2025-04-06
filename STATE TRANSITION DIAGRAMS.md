stateDiagram-v2
    [*] --> Inactive
    Inactive --> Active : Activate
    Active --> Pending : Payment Initiated
    Pending --> Approved : Payment Approved
    Pending --> Declined : Payment Declined
    Declined --> Active : Retry Payment
    Approved --> Used : Card Used
    Used --> Inactive : Deactivate Card
    Active --> Suspended : Suspend Card
    Suspended --> Active : Reactivate Card





    


    
