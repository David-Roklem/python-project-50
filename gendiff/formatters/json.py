import json


def get_json_format(diff: dict):
    '''A json representation of the diff'''
    return json.dumps(diff)
