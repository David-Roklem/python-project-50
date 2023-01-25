import json
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument("-f", "--format", help="set format of output")

    args = parser.parse_args()

    return args


def generate_diff():
    dict_diff = {}
    with open(parse_arguments().first_file, 'r') as first_file:
        if first_file:
            dict1 = json.load(first_file)
        else:
            return ''

    with open(parse_arguments().second_file, 'r') as second_file:
        if second_file:
            dict2 = json.load(second_file)
        else:
            return ''

    # loop for finding common keys
    for key in dict1.keys():
        if dict1[key] == dict2[key]:
            dict_diff[key] = dict1[key]
        else:
            break

    # loop for finding keys only in first file
    for key in dict1.keys():
        if key not in dict2.keys():
            dict_diff[f'- {key}'] = dict1[key]
        else:
            continue

    # loop for finding keys only in second file
    for key in dict2.keys():
        if key not in dict1.keys():
            dict_diff[f'+ {key}'] = dict2[key]
        else:
            continue

    # loop for finding common keys with different values
    for key in dict1.keys():
        if key in dict2.keys() and dict1[key] != dict2[key]:
            dict_diff[f'- {key}'] = dict1[key]
            dict_diff[f'+ {key}'] = dict2[key]
        else:
            continue

    sorted_keys = sorted(dict_diff.keys(), key=lambda x: x.strip('-+ '))
    sorted_dict_diff = {}
    for key in sorted_keys:
        if key in dict_diff:
            sorted_dict_diff[key] = dict_diff[key]

    filling_list = []

    filling_list.append('{')

    for k, v in sorted_dict_diff.items():
        if '+' in k or '-' in k:
            filling_list.append(f'\n  {k}: {v}'.lower())
        else:
            filling_list.append(f'\n    {k}: {v}'.lower())

    filling_list.append('\n}')
    print(''.join(filling_list))
