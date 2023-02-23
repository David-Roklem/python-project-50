import json
import yaml


def parse(data, format_):
    """Parses data"""
    if format_ == 'json':
        return json.loads(data)
    if format_ == 'yaml':
        return yaml.safe_load(data)