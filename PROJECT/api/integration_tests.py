import pytest
from httpx import AsyncClient
from main import app
from sqlmodel import SQLModel, create_engine, Session
from models import VirtualCard

# Test DB setup
TEST_DB_URL = "sqlite:///./test_virtual_cards.db"
test_engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})

@pytest.fixture(autouse=True, scope="module")
def prepare_db():
    SQLModel.metadata.create_all(test_engine)
    yield
    SQLModel.metadata.drop_all(test_engine)

@pytest.mark.asyncio
async def test_crud_card_workflow():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Create card
        response = await client.post("/cards/", json={"holder_name": "Test User"})
        assert response.status_code == 200
        card = response.json()
        card_id = card["id"]
        assert card["holder_name"] == "Test User"
        assert card["balance"] == 0.0

        # Read card
        response = await client.get(f"/cards/{card_id}")
        assert response.status_code == 200
        assert response.json()["holder_name"] == "Test User"

        # Update card
        response = await client.put(f"/cards/{card_id}", json={"holder_name": "Updated User"})
        assert response.status_code == 200
        assert response.json()["holder_name"] == "Updated User"

        # Fund card
        response = await client.post(f"/cards/{card_id}/fund", json={"amount": 100.0})
        assert response.status_code == 200
        assert response.json()["balance"] == 100.0

        # Charge card
        response = await client.post(f"/cards/{card_id}/charge", json={"amount": 25.0})
        assert response.status_code == 200
        assert response.json()["balance"] == 75.0

        # Delete card
        response = await client.delete(f"/cards/{card_id}")
        assert response.status_code == 200

        # Check deleted card
        response = await client.get(f"/cards/{card_id}")
        assert response.status_code == 404
