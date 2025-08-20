import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.db import Base, get_db
from app import models
from app.core.security import create_access_token

# --- DB en memoria para tests (una sola conexión compartida) ---
engine = create_engine(
    "sqlite://",  # importante: sin / para in-memory compartida
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Crear tablas una vez por sesión de tests
@pytest.fixture(scope="session", autouse=True)
def _create_test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


# Override de dependencia get_db para usar la sesión de test
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


# Cliente FastAPI
@pytest.fixture(scope="session")
def client():
    return TestClient(app)


# Helper para crear usuarios
def _create_user(db, email: str, role: str):
    user = models.User(
        email=email,
        password_hash="not-used-in-these-tests",
        role=role,
        name=email.split("@")[0],
        phone=None,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# Headers con token para player
@pytest.fixture(scope="session")
def player_token_headers():
    db = TestingSessionLocal()
    try:
        user = db.query(models.User).filter_by(email="player@example.com").first()
        if not user:
            user = _create_user(db, "player@example.com", "player")
        token = create_access_token({"sub": str(user.id)})
        return {"Authorization": f"Bearer {token}"}
    finally:
        db.close()


# Headers con token para admin
@pytest.fixture(scope="session")
def admin_token_headers():
    db = TestingSessionLocal()
    try:
        user = db.query(models.User).filter_by(email="admin@example.com").first()
        if not user:
            user = _create_user(db, "admin@example.com", "admin")
        token = create_access_token({"sub": str(user.id)})
        return {"Authorization": f"Bearer {token}"}
    finally:
        db.close()
