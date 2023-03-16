from . import JSON, STYLISH, PLAIN
from gendiff.formatters.json import get_json_format
from gendiff.formatters.plain import get_plain_format
from gendiff.formatters.stylish import diff_tree


def apply_formatter(difference: dict, formatter: str) -> str:
    """Apply the selected display format."""
    if formatter == PLAIN:
        return get_plain_format(difference)
    if formatter == STYLISH:
        return diff_tree(difference)
    if formatter == JSON:
        return get_json_format(difference)
    raise ValueError('Incorrect formatter name ({formatter}).')
