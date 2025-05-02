from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4


class VirtualCardBase(SQLModel):
    holder_name: str
    balance: float = 0.0
    is_active: bool = True


class VirtualCard(VirtualCardBase, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)


class VirtualCardCreate(VirtualCardBase):
    pass


class VirtualCardUpdate(SQLModel):
    holder_name: Optional[str] = None
    is_active: Optional[bool] = None


class ChargeRequest(SQLModel):
    amount: float


class FundRequest(SQLModel):
    amount: float
