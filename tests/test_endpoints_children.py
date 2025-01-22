import pytest
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.base import Base  # Replace with your Base model
from app.models.user import User
from app.models.children import Child
from app.schemas.children import ChildCreate, ChildUpdate
from app.api.endpoints.children.functions import (
    create_new_child,
    read_all_children,
    get_child_by_id,
    get_child_by_name,
    update_child,
    delete_child,
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
    child = Child(child_id=1, name="Test Child", age=5, user_id=test_user.user_id)
    db.add(child)
    db.commit()
    db.refresh(child)
    return child


# Test create_new_child
def test_create_new_child(db, test_user):
    child_data = ChildCreate(name="New Child", age=6)
    new_child = create_new_child(db, child_data, test_user)
    assert new_child.name == "New Child"
    assert new_child.age == 6
    assert new_child.user_id == test_user.user_id


# Test read_all_children
def test_read_all_children(db, test_user, test_child):
    children = read_all_children(db, test_user)
    assert len(children) == 1
    assert children[0].name == "Test Child"


# Test get_child_by_id
def test_get_child_by_id(db, test_user, test_child):
    child = get_child_by_id(db, test_child.child_id, test_user)
    assert child.name == "Test Child"


def test_get_child_by_id_not_found(db, test_user):
    with pytest.raises(HTTPException) as exc:
        get_child_by_id(db, 999, test_user)
    assert exc.value.status_code == 404
    assert exc.value.detail == "Child not found or not authorized to access"


# Test get_child_by_name
def test_get_child_by_name(db, test_user, test_child):
    child = get_child_by_name(db, "Test Child", test_user)
    assert child.age == 5


def test_get_child_by_name_not_found(db, test_user):
    with pytest.raises(HTTPException) as exc:
        get_child_by_name(db, "Nonexistent Child", test_user)
    assert exc.value.status_code == 404
    assert exc.value.detail == "Child not found or not authorized to access"


# Test update_child
def test_update_child(db, test_user, test_child):
    updated_data = ChildUpdate(age=6)
    updated_child = update_child(db, test_child.child_id, updated_data, test_user)
    assert updated_child.age == 6


def test_update_child_not_found(db, test_user):
    updated_data = ChildUpdate(age=6)
    with pytest.raises(HTTPException) as exc:
        update_child(db, 999, updated_data, test_user)
    assert exc.value.status_code == 404
    assert exc.value.detail == "Child not found or not authorized to access"


# Test delete_child
def test_delete_child(db, test_user, test_child):
    response = delete_child(db, test_child.child_id, test_user)
    assert response["msg"] == "Test Child deleted successfully"
    children = read_all_children(db, test_user)
    assert len(children) == 0


def test_delete_child_not_found(db, test_user):
    with pytest.raises(HTTPException) as exc:
        delete_child(db, 999, test_user)
    assert exc.value.status_code == 404
    assert exc.value.detail == "Child not found or not authorized to access"
