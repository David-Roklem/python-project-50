import json


def diff_to_json(diff: dict):
    '''A json representation of the diff'''
    return json.dumps(diff)