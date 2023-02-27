from gendiff.file_reader import read_data, get_format
from gendiff.data_parser import parse
from gendiff.data_comparer import compare_data
from gendiff.formatters.formatter import apply_formatter
from gendiff.formatters.formats import STYLISH


def generate_diff(filepath1, filepath2, formatter=STYLISH):
    format1 = get_format(filepath1)
    format2 = get_format(filepath2)
    data1 = parse(read_data(filepath1), format1)
    data2 = parse(read_data(filepath2), format2)
    diff = compare_data(data1, data2)
    return apply_formatter(diff, formatter)


# FAILED tests/test_generate_diff.py::test_generate_diff[tests/fixtures/file1_nested.yml-tests/fixtures/file2_nested.yml-stylish-tests/fixtures/output_stylish_nested] - 
# TypeError: generate_diff() takes 0 positional arguments but 3 were given