import json


def get_mandate_status(json_data):
    data = json.loads(json_data)
    data = list(data.values())
    status = data[0]

    if status in ("Y", "N", "R"):
        return status
    else:
        return "Wrong entry"
