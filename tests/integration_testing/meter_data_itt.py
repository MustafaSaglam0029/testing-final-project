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


def test_get_meter_data(environmental_variables: bool, test_client: TestClient):
    response = test_client.get("/meter/")
    response1 = test_client.get("/meter/?business_partner_id=29292929")
    response2 = test_client.get("/meter/?business_partner_id=0172773192")
    assert response.status_code == 200
    assert response.json() is not None
    assert response1.json() == {"message": "No record for this entry "}
    assert response2.json() == {
        "message": [
            [
                "0172773192",
                "871688540001755533",
                "8716885000005",
                "8712423026766",
                "000000000000060565",
                "1",
                "ES",
                "440.0",
                "589.0",
                "0807952314",
                "01",
                "2027-04-17T00:00:00",
                "2024-08-09T07:38:07",
                "2024-04-18T00:00:00",
            ],
            [
                "0172773192",
                "871688540006140419",
                "8716885000005",
                "8712423026766",
                "000000003401381299",
                "1",
                "ES",
                "1326.0",
                None,
                "0807952315",
                "02",
                "2027-04-17T00:00:00",
                "2024-08-09T07:38:07",
                "2024-04-18T00:00:00",
            ],
        ]
    }


def test_post_meter_data(environmental_variables: bool, test_client: TestClient):
    payload = {
        "business_partner_id": "0102030405",
        "connection_ean_code": "871694840008848452",
        "grid_company_code": "8716948000003",
        "oda_code": "8712423026766",
        "meter_number": "000000000000147662",
        "smart_collectable": "1",
        "brand": "ES",
        "sjv1": "2980.0",
        "sjv2": "4304.0",
        "installation": "0801225657",
        "division": "01",
        "move_out_date": "2024-10-27 00:00:00",
        "row_create_datetime": "2024-08-09 07:38:07",
        "move_in_date": "2022-01-21 00:00:00",
    }
    response = test_client.post("/meter/", json=payload)
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json() == {
        "message": "Record for 0102030405 is created successfully"
    }


def test_put_meter_data(environmental_variables: bool, test_client: TestClient):

    payload = {"smart_collectable": "0"}

    response = test_client.put("/meter/0172773232", json=payload)
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json() == {
        "message": "Record for 0172773232 is changed successfully"
    }


def test_del_meter_data(environmental_variables: bool, test_client: TestClient):
    response = test_client.delete("/meter/0172773248")
    response1 = test_client.delete("/meter/0101010101")
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json() == {
        "message": "Record for 0172773248 is deleted successfully"
    }
    assert response1.json() == {"message": f"No record for 0101010101"}
