from src.models.meter_readings_model import IncomingMeterReadings
from src.utils.get_meter_readings_status import get_validation_status


# Data is coming in a certain format

data1 = {"validation_status": ""}
data1 = IncomingMeterReadings(**data1)
data1 = data1.model_dump_json()

data2 = {"validation_status": "Not"}
data2 = IncomingMeterReadings(**data2)
data2 = data2.model_dump_json()

data3 = {"validation_status": "VALID"}
data3 = IncomingMeterReadings(**data3)
data3 = data3.model_dump_json()


def test_get_meter_collectable():
    response_one = get_validation_status(data1)
    response_two = get_validation_status(data2)
    response_three = get_validation_status(data3)
    assert response_one == "Wrong entry"
    assert response_two == "Wrong entry"
    assert response_three == "VALID"
