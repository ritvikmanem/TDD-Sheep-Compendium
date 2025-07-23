from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")
    
    assert response.status_code == 200

    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }
    
def test_add_sheep():
    sheep_data_name = {
        "id": 7,  
        "name": "Garry",
        "breed": "Suffolk",
        "sex": "ewe"
    }
    
    response = client.post("/sheep", json=sheep_data_name)
       
    assert response.status_code == 201
    
    created_sheep = response.json()
    assert "id" in created_sheep
    assert created_sheep["name"] == sheep_data_name["name"]
    assert created_sheep["breed"] == sheep_data_name["breed"]
    assert created_sheep["sex"] == sheep_data_name["sex"]
