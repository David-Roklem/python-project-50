import json
import yaml


def parse(data, format_: str) -> str:
    """Parses data"""
    if format_ == 'json':
        parsed_data = json.loads(data)
        return parsed_data
    elif format_ in ['yaml', 'yml']:
        parsed_data = yaml.safe_load(data)
        return parsed_data
    raise TypeError(
        'The file extension (.{format_}) is not supported.\n'
        'Make sure that the selected files have '
        'the extension: json, yaml or yml.'.format(format_=format_)
    )
