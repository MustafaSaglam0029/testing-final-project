from fastapi.testclient import TestClient
from src.router import api_router
from pytest import fixture
import os


@fixture
def environmental_variables():
    os.environ["dbname"] = "postgres"
    os.environ["host"] = "127.0.0.1"
    os.environ["user"] = "postgres"
    os.environ["password"] = "1234"
    os.environ["port"] = "5432"
    return True


@fixture
def test_client():
    return TestClient(api_router, "http://127.0.0.1:8080")


def test_get_mandate_data(environmental_variables: bool, test_client: TestClient):
    response = test_client.get("/mandate/")
    response1 = test_client.get("/mandate/?business_partner_id=29292929")
    response2 = test_client.get("/mandate/?business_partner_id=2929292929")
    assert response.status_code == 200
    assert response.json() is not None
    assert response1.json() == {"message": "No record for this entry"}
    assert response2.json() == {
        "message": [
            [
                "2929292929",
                "Y",
                "D",
                "ES",
                "2024-04-25T12:06:43",
                "2019-07-02T10:00:00",
                "SYSTEM",
                "292929",
                "P4",
                "daily_insight",
            ]
        ]
    }


def test_post_mandate_data(environmental_variables: bool, test_client: TestClient):
    payload = {
        "business_partner_id": "1515151515",
        "mandate_status": "Y",
        "collection_frequency": "D",
        "brand": "ES",
        "row_update_datetime": "2024-04-25 12:06:43",
        "row_create_datetime": "2019-07-02 10:00:00",
        "changed_by": "SYSTEM",
        "mandate_id": "292929",
        "collection_type": "P4",
        "metering_consent": "daily_insight",
    }
    response = test_client.post("/mandate/", json=payload)
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json() == {
        "message": "Record for 1515151515 is created successfully"
    }


def test_put_mandate_data(environmental_variables: bool, test_client: TestClient):

    payload = {"mandate_status": "Y"}

    response = test_client.put("/mandate/0101869662", json=payload)
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json() == {
        "message": "Record for 0101869662 is changed successfully"
    }


def test_del_mandate_data(environmental_variables: bool, test_client: TestClient):
    response = test_client.delete("/mandate/0131040176")
    response1 = test_client.delete("/mandate/0101010101")
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json() == {
        "message": "Record for 0131040176 is deleted successfully"
    }
    assert response1.json() == {"message": f"No record for 0101010101"}
