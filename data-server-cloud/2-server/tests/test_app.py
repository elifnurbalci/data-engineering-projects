from fastapi.testclient import TestClient
from api.app import app
import pytest

client = TestClient(app)

@pytest.mark.it('unit test: healthcheck responds correctly')
def test_handle_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "Everything is fine!"}  # Ensure this matches your actual return

@pytest.mark.it('unit test: get doughnuts info without parameters')
def test_get_doughnuts_info_no_params():
    response = client.get("/doughnuts/info")
    assert response.status_code == 200
    assert "results" in response.json()

@pytest.mark.it('unit test: get doughnuts info with max_calories and nuts parameters')
def test_get_doughnuts_info_with_params():
    response = client.get("/doughnuts/info?max_calories=700&nuts=true")
    assert response.status_code == 200
    results = response.json()["results"]
    assert all(doughnut["calories"] <= 700 and doughnut["contains_nuts"] is True for doughnut in results)
