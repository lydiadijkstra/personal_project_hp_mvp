import pytest
from unittest.mock import patch
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.base import Base  # Replace with your Base model
from app.models.user import User
from app.models.children import Child
from app.models.tips import Tip
from app.schemas.tips import TipCreate
from app.api.endpoints.tips.functions import (
    create_new_tip,
    read_all_tips,
    get_tip_by_id,
)

# Setup in-memory SQLite database
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency
@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)  # Create tables
    db = TestingSessionLocal()
    yield db
    db.close()

@pytest.fixture
def test_user(db):
    user = User(user_id=1, user_name="testuser", email="test@example.com", password="hashedpassword")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@pytest.fixture
def test_child(db, test_user):
    child = Child(child_id=1, name="Test Child", age=5, difficulty="hitting", user_id=test_user.user_id)
    db.add(child)
    db.commit()
    db.refresh(child)
    return child

@pytest.fixture
def test_tip(db, test_user, test_child):
    tip = Tip(tip_id=1, user_id=test_user.user_id, child_id=test_child.child_id, problem_type="hitting", content="Example Tip")
    db.add(tip)
    db.commit()
    db.refresh(tip)
    return tip


# Mock the AI tip generation function
@patch("app.core.gemini_api_datafetcher.get_ai_tip")
def test_create_new_tip(mock_get_ai_tip, db, test_user, test_child):
    mock_get_ai_tip.return_value = "AI-generated Tip"

    tip_data = TipCreate(problem_type="hitting")
    new_tip = create_new_tip(db, tip_data, test_user, test_child.child_id)

    assert new_tip.content == "AI-generated Tip"
    assert new_tip.user_id == test_user.user_id
    assert new_tip.child_id == test_child.child_id
    mock_get_ai_tip.assert_called_once_with(problem_type="hitting")


# Test create_new_tip with missing child
@patch("app.core.gemini_api_datafetcher.get_ai_tip")
def test_create_new_tip_child_not_found(mock_get_ai_tip, db, test_user):
    mock_get_ai_tip.return_value = "AI-generated Tip"

    tip_data = TipCreate(problem_type="hitting")
    with pytest.raises(HTTPException) as exc:
        create_new_tip(db, tip_data, test_user, child_id=999)  # Invalid child ID
    assert exc.value.status_code == 404
    assert exc.value.detail == "Child not found or not authorized to access"


# Test read_all_tips
def test_read_all_tips(db, test_user, test_tip):
    tips = read_all_tips(db, test_user)
    assert len(tips) == 1
    assert tips[0].content == "Example Tip"


# Test get_tip_by_id
def test_get_tip_by_id(db, test_user, test_tip):
    tip = get_tip_by_id(db, test_tip.tip_id, test_user)
    assert tip.content == "Example Tip"
    assert tip.tip_id == test_tip.tip_id


# Test get_tip_by_id with invalid ID
def test_get_tip_by_id_not_found(db, test_user):
    with pytest.raises(HTTPException) as exc:
        get_tip_by_id(db, tip_id=999, current_user=test_user)  # Invalid tip ID
    assert exc.value.status_code == 404
    assert exc.value.detail == "Tip not found or not authorized to access"


# Test get_tip_by_id for unauthorized access
def test_get_tip_by_id_unauthorized(db, test_user, test_tip):
    # Create a new user (unauthorized to access the test_tip)
    another_user = User(user_id=2, user_name="anotheruser", email="another@example.com", password="hashedpassword")
    db.add(another_user)
    db.commit()

    with pytest.raises(HTTPException) as exc:
        get_tip_by_id(db, tip_id=test_tip.tip_id, current_user=another_user)
    assert exc.value.status_code == 404
    assert exc.value.detail == "Tip not found or not authorized to access"
