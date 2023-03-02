"""In this module a stylish diff is represented. It is built
upon the basis of the main logic implemented in gendiff/diff.py"""
import json
from itertools import chain
from typing import Any


STATE = {
    'new': '  + ',
    'removed': '  - ',
    'equal': '    ',
}

REPLACER = ' '
SPACES_COUNT = 4
INDENT = REPLACER * SPACES_COUNT


def stringify_value(checked_value: Any, depth):
    """Check and convert value if it's dict.
    Parameters:
        checked_value: stringify the value.
        depth: indent depth.
    Returns:
        string_list: string with right indent.
    """
    if not isinstance(checked_value, dict):
        return checked_value
    string_list = ['{']
    spaces = INDENT * depth
    for key, current_value in checked_value.items():
        if isinstance(checked_value, dict):
            current_value = stringify_value(current_value, depth + 1)
        string = '{spaces}{indent}{key}: {value}'.format(
            spaces=spaces,
            indent=INDENT,
            key=key,
            value=current_value,
        )
        string_list.append(string)
    string_list.append('{spaces}}}'.format(spaces=spaces))
    return '\n'.join(string_list)


def get_stylish_format(diff_file: dict):
    """Generate list of strings with highlighted differences.
    Parameters:
        diff_file: dict with differences.
    Returns:
        apply_formatter(difference, formatter):
        output of the resulting difference in the selected format.
    """

    def inner(diff_dict: dict, depth):
        result_list = []
        space = INDENT * depth
        for key, diff_val in diff_dict.items():
            status = diff_val.get('status')
            current_value = diff_val.get('value')
            if status == 'inserted':
                result_list.append(
                    '{space}{indent}{key}: {inserted_value}'.format(
                        space=space,
                        indent=INDENT,
                        key=key,
                        inserted_value=inner(current_value, depth + 1),
                    ),
                )
            elif status == 'updated':
                result_list.append('{space}{flag}{key}: {old_value}'.format(
                    space=space,
                    flag=STATE.get('removed'),
                    key=key,
                    old_value=stringify_value(
                        current_value.get('old'),
                        depth + 1,
                    ),
                ),
                )
                result_list.append('{space}{flag}{key}: {new_value}'.format(
                    space=space,
                    flag=STATE.get('new'),
                    key=key,
                    new_value=stringify_value(
                        current_value.get('new'),
                        depth + 1,
                    ),
                ),
                )
            else:
                result_list.append('{space}{flag}{key}: {value}'.format(
                    space=space,
                    flag=STATE.get(status),
                    key=key,
                    value=stringify_value(current_value, depth + 1),
                ),
                )
        return '\n'.join(chain('{', result_list, [space + '}']))

    converted_file = to_string(diff_file)
    return inner(converted_file, depth=0)


def to_string(diff_file: dict) -> str:
    """Convert the bool & None values to string."""
    for key, diff_value in diff_file.items():
        if isinstance(diff_value, (bool, type(None))):
            diff_file[key] = json.dumps(diff_value)
            # if diff_value:
            #     diff_file[key] = 'true'
            # elif not diff_value:
            #     diff_file[key] = 'false'
            # elif diff_value is None:
            #     diff_file[key] = 'null'
        elif isinstance(diff_value, dict):
            to_string(diff_value)
    return diff_file
