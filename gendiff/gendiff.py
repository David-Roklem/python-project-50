from gendiff.file_reader import read_data, get_format
from gendiff.data_parser import parse
from gendiff.data_comparer import build_diff
from gendiff.formatters.formatter import apply_formatter
from .formatters import STYLISH


def generate_diff(filepath1, filepath2, formatter=STYLISH):
    format1 = get_format(filepath1)
    format2 = get_format(filepath2)
    data1 = parse(read_data(filepath1), format1)
    data2 = parse(read_data(filepath2), format2)
    diff = build_diff(data1, data2)
    return apply_formatter(diff, formatter)
