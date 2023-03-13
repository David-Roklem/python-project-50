import json
import yaml


def parse(data, format_: str) -> str:
    """Parses data"""
    if format_ == 'json':
        return json.loads(data)
    elif format_ in ['yaml', 'yml']:
        return yaml.safe_load(data)
    raise TypeError(
        'The file extension (.{format_}) is not supported.\n'
        'Make sure that the selected files have '
        'the extension: json, yaml or yml.'.format(format_=format_)
    )
