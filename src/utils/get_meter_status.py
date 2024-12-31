import json


def get_meter_collectable(json_data):
    data = json.loads(json_data)
    data = list(data.values())
    status = data[0]

    if status in ("1", "0"):
        return status
    else:
        return "Wrong entry"
