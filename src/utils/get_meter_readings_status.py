import json


def get_validation_status(json_data):
    data = json.loads(json_data)
    data = list(data.values())
    status = data[0]

    if status in ("VALID", "INVALID"):
        return status
    else:
        return "Wrong entry"
