from src.utils.get_mandate_status import get_mandate_status
from src.models.mandate_data_model import IncomingMandateData


# Data is coming in a certain format

data1 = {"mandate_status": ""}
data1 = IncomingMandateData(**data1)
data1 = data1.model_dump_json()

data2 = {"mandate_status": "A"}
data2 = IncomingMandateData(**data2)
data2 = data2.model_dump_json()

data3 = {"mandate_status": "Y"}
data3 = IncomingMandateData(**data3)
data3 = data3.model_dump_json()


def test_get_mandate_status():
    response_one = get_mandate_status(data1)
    response_two = get_mandate_status(data2)
    response_three = get_mandate_status(data3)
    assert response_one == "Wrong entry"
    assert response_two == "Wrong entry"
    assert response_three == "Y"
