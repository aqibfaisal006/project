import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_health(client):
    res = client.get('/api/health')
    assert res.status_code == 200


def test_get_students(client):
    res = client.get('/students')
    assert res.status_code == 200


def test_get_nonexistent_student(client):
    res = client.get('/students/999')
    assert res.status_code == 404


def test_add_student(client):
    res = client.post('/students', json={"name": "Ali"})
    assert res.status_code == 201


def test_add_student_missing_field(client):
    res = client.post('/students', json={})
    assert res.status_code == 400