from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import uuid

@dataclass
class User:
    id: str
    name: str
    email: str

@dataclass
class VirtualCard:
    id: str
    user_id: str
    card_number: str
    expiry_date: str
    balance: float

@dataclass
class Transaction:
    id: str
    card_id: str
    amount: float
    timestamp: datetime
    description: Optional[str] = None
