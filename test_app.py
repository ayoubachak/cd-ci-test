import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index(app, client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Hello, world!" in res.data

def test_hello(app, client):
    name = "ayoub"
    res = client.get(f"/hello/{name}")
    assert res.status_code == 200
    assert bytes(f"Hello, {name}!", 'utf-8') in res.data

