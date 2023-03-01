"""
In this module two dictionaries are compared.
As a result the main func compare_data returns
dictionary that represents the difference between two
input dicts.
"""


def compare_data(data1: dict, data2: dict) -> dict:
    """Find the different between two files.
    """
    result_diff = {}
    sorted_keys = sorted(set.union(set(data1), set(data2)))
    for key in sorted_keys:
        if key not in data1:
            status = 'new'
            ident_value = data2.get(key)
        elif key not in data2:
            status = 'removed'
            ident_value = data1.get(key)
        elif data1.get(key) == data2.get(key):
            status = 'equal'
            ident_value = data2.get(key)
        elif all(
            [
                isinstance(data1.get(key), dict),
                isinstance(data2.get(key), dict),
            ],
        ):
            status, ident_value = 'inserted', compare_data(
                data1.get(key),
                data2.get(key),
            )
        else:
            status = 'updated'
            ident_value = {
                'old': data1.get(key),
                'new': data2.get(key),
            }
        result_diff[key] = {
            'status': '{status}'.format(status=status),
            'value': ident_value,
        }
    return result_diff
