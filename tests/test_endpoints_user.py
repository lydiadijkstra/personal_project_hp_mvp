import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.models.user import Base, User
from app.schemas.user import UserCreate, UserUpdate
from app.core.dependencies import get_db
from datetime import timedelta
from jose import jwt

# Database configuration for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# Test data
TEST_USER = {
    "user_name": "testuser",
    "email": "testuser@example.com",
    "password": "password123",
    "name": "Test User",
    "location": "Test Location",
    "role": "user",
}

@pytest.fixture
def create_test_user():
    db = next(override_get_db())
    hashed_password = "$2b$12$somethinghashed"  # Replace with an actual hashed password
    new_user = User(
        user_name=TEST_USER["user_name"],
        email=TEST_USER["email"],
        password=hashed_password,
        name=TEST_USER["name"],
        location=TEST_USER["location"],
        role=TEST_USER["role"],
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    yield new_user
    db.delete(new_user)
    db.commit()

# Unit tests

def test_create_new_user():
    response = client.post(
        "/users/", json=TEST_USER  # Adjust the endpoint as per your FastAPI app
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == TEST_USER["email"]

def test_get_user_by_email(create_test_user):
    db = next(override_get_db())
    from app.dependencies import get_user_by_email  # Import your actual function
    user = get_user_by_email(db, TEST_USER["email"])
    assert user.email == TEST_USER["email"]

def test_update_user(create_test_user):
    update_data = {"name": "Updated User"}
    response = client.put(
        f"/users/{create_test_user.user_id}", json=update_data
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated User"

def test_delete_user(create_test_user):
    response = client.delete(f"/users/{create_test_user.user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["msg"] == f"{create_test_user.email} deleted successfully"

def test_authenticate_user(create_test_user):
    login_data = {"email": TEST_USER["email"], "password": "password123"}
    response = client.post("/auth/login", json=login_data)
    assert response.status_code == 200
    token_data = response.json()
    assert "access_token" in token_data

def test_create_access_token():
    from app.dependencies import create_access_token  # Import your actual function
    data = {"sub": "testuser"}
    token = create_access_token(data, timedelta(minutes=15))
    assert jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

