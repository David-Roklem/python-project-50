from .file_reader import load_file


def generate_diff(file_path_1, file_path_2):

    dict_diff = {}

    dict1 = load_file(file_path_1)

    dict2 = load_file(file_path_2)

    # loop for finding common keys
    for key in dict1.keys():
        if dict1[key] == dict2[key]:
            dict_diff[f'  {key}'] = dict1[key]
        else:
            break

    # loop for finding keys only in first file
    for key in dict1.keys():
        if key not in dict2.keys():
            dict_diff[f'  - {key}'] = dict1[key]
        else:
            continue

    # loop for finding keys only in second file
    for key in dict2.keys():
        if key not in dict1.keys():
            dict_diff[f'  + {key}'] = dict2[key]
        else:
            continue

    # loop for finding common keys with different values
    for key in dict1.keys():
        if key in dict2.keys() and dict1[key] != dict2[key]:
            dict_diff[f'  - {key}'] = dict1[key]
            dict_diff[f'  + {key}'] = dict2[key]
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
    result_string = ''.join(filling_list)
    return result_string
