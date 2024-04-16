import pytest
from app import app
from flask import Flask
from models import db  # Import the db object from the appropriate module

@pytest.fixture
def client():
    # Set up the test client
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
    with app.test_client() as client:
        with app.app_context():
            # Inicializar la base de datos
            db.create_all()
            try:
                yield client
            finally:
                # Revertir los cambios después de la prueba
                db.session.rollback()

# Tests for the endpoint /
def test_root(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the My Globant Test Application' in response.data  # Check if the content is as expected

# Tests for the endpoint /upload_csv_form
def test_upload_csv_form(client):
    response = client.get('/upload_csv_form')
    assert response.status_code == 200
    assert b'Upload CSV' in response.data  # Check if the content is as expected

# Tests for the endpoint /upload_csv
def test_upload_csv(client):
    with open('departments.csv', 'rb') as file:

        response = client.post('/upload_csv', data={'file': file})
        assert response.status_code == 200
        assert b'File uploaded and processed successfully' in response.data

    # Test with unsupported file type
    with open('jobs.txt', 'rb') as file:
        response = client.post('/upload_csv', data={'file': file})
        assert response.status_code == 400
        assert b'Unsupported file type' in response.data

# Tests for the endpoint /metrics/departments_above_mean
def test_departments_above_mean(client):
    response = client.get('/metrics/departments_above_mean')
    assert response.status_code == 200
