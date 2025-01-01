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


def test_get_meter_readings(environmental_variables: bool, test_client: TestClient):
    response = test_client.get("/meter_readings/")
    response1 = test_client.get("/meter_readings/?connection_ean_code=29292929")
    response2 = test_client.get(
        "/meter_readings/?connection_ean_code=871694840007974299"
    )
    assert response.status_code == 200
    assert response.json() is not None
    assert response1.json() == {"message": "No record for this entry "}
    assert response2.json() == {
        "message": [
            [
                "0100000219",
                "ESSENT",
                "871694840007974299",
                "ELECTRICITY",
                "51402565",
                "2023-11-01",
                '{"supplyLow": 8771.102, "supplyHigh": 13139.172, "returnLow": 651.858, "returnHigh": 1286.793}',
                None,
                None,
                "VALID",
            ],
            [
                "0100000219",
                "ESSENT",
                "871694840007974299",
                "ELECTRICITY",
                "51402565",
                "2024-01-01",
                '{"supplyLow": 8886.618, "supplyHigh": 13293.333, "returnLow": 666.136, "returnHigh": 1316.481}',
                None,
                None,
                "VALID",
            ],
            [
                "0100000219",
                "ESSENT",
                "871694840007974299",
                "ELECTRICITY",
                "51402565",
                "2024-02-01",
                '{"supplyLow": 8938.348, "supplyHigh": 13365.289, "returnLow": 681.854, "returnHigh": 1356.235}',
                None,
                None,
                "VALID",
            ],
            [
                "0100000219",
                "ESSENT",
                "871694840007974299",
                "ELECTRICITY",
                "51402565",
                "2024-03-01",
                '{"supplyLow": 8982.253, "supplyHigh": 13428.337, "returnLow": 691.305, "returnHigh": 1382.008}',
                None,
                None,
                "VALID",
            ],
            [
                "0100000219",
                "ESSENT",
                "871694840007974299",
                "ELECTRICITY",
                "51402565",
                "2023-12-01",
                '{"supplyLow": 8818.035, "supplyHigh": 13211.605, "returnLow": 659.76, "returnHigh": 1314.703}',
                None,
                None,
                "VALID",
            ],
            [
                "0100000219",
                "ESSENT",
                "871694840007974299",
                "ELECTRICITY",
                "51402565",
                "2024-04-01",
                '{"returnLow": 757.51, "supplyLow": 9021.462, "returnHigh": 1463.065, "supplyHigh": 13483.59}',
                None,
                None,
                "VALID",
            ],
            [
                "0100000219",
                "ESSENT",
                "871694840007974299",
                "ELECTRICITY",
                "51402565",
                "2024-05-01",
                '{"returnLow": 831.812, "supplyLow": 9053.833, "returnHigh": 1589.765, "supplyHigh": 13522.708}',
                None,
                None,
                "VALID",
            ],
            [
                "0100000219",
                "ESSENT",
                "871694840007974299",
                "ELECTRICITY",
                "51402565",
                "2024-06-01",
                '{"returnLow": 935.184, "supplyLow": 9085.74, "returnHigh": 1780.992, "supplyHigh": 13551.19}',
                None,
                None,
                "VALID",
            ],
            [
                "0100000219",
                "ESSENT",
                "871694840007974299",
                "ELECTRICITY",
                "51402565",
                "2024-07-01",
                '{"returnLow": 1027.195, "supplyLow": 9114.707, "returnHigh": 1957.158, "supplyHigh": 13574.605}',
                None,
                None,
                "VALID",
            ],
            [
                "0100000219",
                "ESSENT",
                "871694840007974299",
                "ELECTRICITY",
                "51402565",
                "2024-08-01",
                '{"returnLow": 1100.202, "supplyLow": 9146.67, "returnHigh": 2166.669, "supplyHigh": 13605.256}',
                None,
                None,
                "VALID",
            ],
        ]
    }


def test_post_meter_readings(environmental_variables: bool, test_client: TestClient):
    payload = {
        "account_id": "0100000219",
        "brand": "ESSENT",
        "connection_ean_code": "871694840015809705",
        "energy_type": "GAS",
        "meter_number": "13041698",
        "reading_date": "2023-11-01",
        "reading_electricity": None,
        "reading_gas": {"gasTotal": 17829.873},
        "rejection": None,
        "validation_status": "VALID",
    }
    response = test_client.post("/meter_readings/", json=payload)
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json() == {
        "message": "Record for 0100000219 is created successfully"
    }


def test_put_meter_readings(environmental_variables: bool, test_client: TestClient):

    payload = {"validation_status": "INVALID"}

    response = test_client.put("/meter_readings/0100000157", json=payload)
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json() == {
        "message": "Record for 0100000157 is changed successfully"
    }


def test_del_meter_readings(environmental_variables: bool, test_client: TestClient):
    response = test_client.delete("/meter_readings/0100000270")
    response1 = test_client.delete("/meter_readings/0202020202")
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json() == {
        "message": "Record for 0100000270 is deleted successfully"
    }
    assert response1.json() == {"message": f"No record for 0202020202"}
