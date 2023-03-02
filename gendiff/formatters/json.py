import json


def get_json_format(diff: dict):
    """Json representation of the diff."""
    return json.dumps(diff)
