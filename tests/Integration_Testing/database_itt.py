from fastapi.testclient import TestClient
from src.router import api_router
from src.utils.db_connection import select
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

def test_select(environmental_variables: bool, test_client: TestClient):
    output = select()
    assert output is not None
    assert output == [('0132158868',)]


