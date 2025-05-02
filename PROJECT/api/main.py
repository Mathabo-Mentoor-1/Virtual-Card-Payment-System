from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Session, create_engine, select
from models import VirtualCard, VirtualCardCreate, VirtualCardUpdate, ChargeRequest, FundRequest

app = FastAPI()

# SQLite in-memory for simplicity
engine = create_engine("sqlite:///virtual_cards.db")
SQLModel.metadata.create_all(engine)

@app.post("/cards/", response_model=VirtualCard)
def create_card(card: VirtualCardCreate):
    new_card = VirtualCard(**card.dict())
    with Session(engine) as session:
        session.add(new_card)
        session.commit()
        session.refresh(new_card)
        return new_card

@app.get("/cards/{card_id}", response_model=VirtualCard)
def read_card(card_id: str):
    with Session(engine) as session:
        card = session.get(VirtualCard, card_id)
        if not card:
            raise HTTPException(status_code=404, detail="Card not found")
        return card

@app.put("/cards/{card_id}", response_model=VirtualCard)
def update_card(card_id: str, card_update: VirtualCardUpdate):
    with Session(engine) as session:
        card = session.get(VirtualCard, card_id)
        if not card:
            raise HTTPException(status_code=404, detail="Card not found")
        for key, value in card_update.dict(exclude_unset=True).items():
            setattr(card, key, value)
        session.commit()
        session.refresh(card)
        return card

@app.delete("/cards/{card_id}")
def delete_card(card_id: str):
    with Session(engine) as session:
        card = session.get(VirtualCard, card_id)
        if not card:
            raise HTTPException(status_code=404, detail="Card not found")
        session.delete(card)
        session.commit()
        return {"detail": "Card deleted"}

@app.post("/cards/{card_id}/fund", response_model=VirtualCard)
def fund_card(card_id: str, fund: FundRequest):
    with Session(engine) as session:
        card = session.get(VirtualCard, card_id)
        if not card or not card.is_active:
            raise HTTPException(status_code=404, detail="Active card not found")
        card.balance += fund.amount
        session.commit()
        session.refresh(card)
        return card

@app.post("/cards/{card_id}/charge", response_model=VirtualCard)
def charge_card(card_id: str, charge: ChargeRequest):
    with Session(engine) as session:
        card = session.get(VirtualCard, card_id)
        if not card or not card.is_active:
            raise HTTPException(status_code=404, detail="Active card not found")
        if card.balance < charge.amount:
            raise HTTPException(status_code=400, detail="Insufficient balance")
        card.balance -= charge.amount
        session.commit()
        session.refresh(card)
        return card
