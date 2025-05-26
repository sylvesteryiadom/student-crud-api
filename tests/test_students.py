import pytest
from app import create_app, db

@pytest.fixture
def client():
    # Pass test config to override DB URI before init_app
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    })
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_healthcheck(client):
    resp = client.get('/healthcheck')
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}

def test_create_student(client):
    resp = client.post('/api/v1/students', json={
        "name": "Alice",
        "email": "alice@example.com",
        "age": 21
    })
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"
    assert data["age"] == 21

def test_get_students(client):
    # Create a student first
    client.post('/api/v1/students', json={
        "name": "Bob",
        "email": "bob@example.com"
    })
    resp = client.get('/api/v1/students')
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert any(s["email"] == "bob@example.com" for s in data)

def test_get_student_by_id(client):
    # Create a student
    resp = client.post('/api/v1/students', json={
        "name": "Carol",
        "email": "carol@example.com"
    })
    student_id = resp.get_json()["id"]
    # Retrieve by ID
    resp = client.get(f'/api/v1/students/{student_id}')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["email"] == "carol@example.com"

def test_update_student(client):
    # Create a student
    resp = client.post('/api/v1/students', json={
        "name": "Dave",
        "email": "dave@example.com"
    })
    student_id = resp.get_json()["id"]
    # Update student
    resp = client.put(f'/api/v1/students/{student_id}', json={
        "name": "David"
    })
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["name"] == "David"

def test_delete_student(client):
    # Create a student
    resp = client.post('/api/v1/students', json={
        "name": "Eve",
        "email": "eve@example.com"
    })
    student_id = resp.get_json()["id"]
    # Delete student
    resp = client.delete(f'/api/v1/students/{student_id}')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["message"] == "Student deleted"
    # Verify deletion
    resp = client.get(f'/api/v1/students/{student_id}')
    assert resp.status_code == 404

def test_create_student_missing_fields(client):
    resp = client.post('/api/v1/students', json={"name": "NoEmail"})
    assert resp.status_code == 400

def test_get_student_not_found(client):
    resp = client.get('/api/v1/students/999')
    assert resp.status_code == 404

def test_update_student_not_found(client):
    resp = client.put('/api/v1/students/999', json={"name": "Ghost"})
    assert resp.status_code == 404

def test_delete_student_not_found(client):
    resp = client.delete('/api/v1/students/999')
    assert resp.status_code == 404
