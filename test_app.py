import pytest
from app import app, db, Todo

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    # Clean up after test
    with app.app_context():
        db.drop_all()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_add_todo(client):
    response = client.post('/add', data={'title': 'Test Todo'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Test Todo' in response.data

def test_update_todo(client):
    # Add a todo first
    client.post('/add', data={'title': 'Test Todo'})
    todo = Todo.query.first()
    response = client.get(f'/update/{todo.id}')
    assert response.status_code == 302  # Redirect
    updated_todo = Todo.query.first()
    assert updated_todo.complete == True

def test_delete_todo(client):
    # Add a todo first
    client.post('/add', data={'title': 'Test Todo'})
    todo = Todo.query.first()
    response = client.get(f'/delete/{todo.id}')
    assert response.status_code == 302  # Redirect
    assert Todo.query.first() is None
