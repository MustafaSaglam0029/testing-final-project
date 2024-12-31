from src.utils.get_meter_status import get_meter_collectable
from src.models.meter_data_model import IncomingMeterData

# Data is coming in a certain format

data1 = {"smart_collectable": ""}
data1 = IncomingMeterData(**data1)
data1 = data1.model_dump_json()

data2 = {"smart_collectable": "5"}
data2 = IncomingMeterData(**data2)
data2 = data2.model_dump_json()

data3 = {"smart_collectable": "1"}
data3 = IncomingMeterData(**data3)
data3 = data3.model_dump_json()


def test_get_meter_collectable():
    response_one = get_meter_collectable(data1)
    response_two = get_meter_collectable(data2)
    response_three = get_meter_collectable(data3)
    assert response_one == "Wrong entry"
    assert response_two == "Wrong entry"
    assert response_three == "1"
