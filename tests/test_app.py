import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import app

app_instance = FastAPI()
app_instance.mount("/", app.app)
client = TestClient(app.app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

def test_signup_and_unregister():
    activity = "Chess Club"
    email = "pytestuser@mergington.edu"
    # Signup
    response = client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code in (200, 400)  # 400 if already signed up
    # Unregister
    response = client.post(f"/activities/{activity}/unregister?email={email}")
    assert response.status_code in (200, 404)  # 404 if not found
