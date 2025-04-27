from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

@dataclass
class User:
    id: int
    name: str
    email: str

@dataclass
class VirtualCard:
    id: int
    user_id: int
    card_number: str
    expiration_date: datetime
    cvv: str
    is_active: bool = True  # Default to active unless specified otherwise

@dataclass
class Transaction:
    id: int
    card_id: int
    amount: float
    timestamp: datetime = field(default_factory=datetime.now)
    merchant: str

