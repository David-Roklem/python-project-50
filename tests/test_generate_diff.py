import pytest
from gendiff.gendiff import generate_diff


OUTPUT_STYLISH_FLAT = 'tests/fixtures/output_stylish_flat'
OUTPUT_STYLISH_NESTED = 'tests/fixtures/output_stylish_nested'
OUTPUT_PLAIN_FLAT = 'tests/fixtures/output_plain_flat'
OUTPUT_PLAIN_NESTED = 'tests/fixtures/output_plain_nested'
OUTPUT_JSON_FLAT = 'tests/fixtures/output_json_flat'
OUTPUT_JSON_NESTED = 'tests/fixtures/output_json_nested'
JSON_FLAT_FL1 = 'tests/fixtures/file1.json'
JSON_FLAT_FL2 = 'tests/fixtures/file2.json'
YAML_FLAT_FL1 = 'tests/fixtures/file1.yaml'
YAML_FLAT_FL2 = 'tests/fixtures/file2.yaml'
YML_FLAT_FL1 = 'tests/fixtures/file1.yml'
YML_FLAT_FL2 = 'tests/fixtures/file2.yml'
JSON_TREE_FL1 = 'tests/fixtures/file1_nested.json'
JSON_TREE_FL2 = 'tests/fixtures/file2_nested.json'
YAML_TREE_FL1 = 'tests/fixtures/file1_nested.yaml'
YAML_TREE_FL2 = 'tests/fixtures/file2_nested.yaml'
YML_TREE_FL1 = 'tests/fixtures/file1_nested.yml'
YML_TREE_FL2 = 'tests/fixtures/file2_nested.yml'

FORMATTERS = (
    'stylish',
    'plain',
    'json',
)


@pytest.mark.parametrize(
    ('argument1', 'argument2', 'formatter', 'expected'),
    (
        (JSON_FLAT_FL1, JSON_FLAT_FL2, FORMATTERS[0], OUTPUT_STYLISH_FLAT),
        (YAML_FLAT_FL1, YAML_FLAT_FL2, FORMATTERS[0], OUTPUT_STYLISH_FLAT),
        (YML_FLAT_FL1, YML_FLAT_FL2, FORMATTERS[0], OUTPUT_STYLISH_FLAT),
        (JSON_TREE_FL1, JSON_TREE_FL2, FORMATTERS[0], OUTPUT_STYLISH_NESTED),
        (YAML_TREE_FL1, YAML_TREE_FL2, FORMATTERS[0], OUTPUT_STYLISH_NESTED),
        (YML_TREE_FL1, YML_TREE_FL2, FORMATTERS[0], OUTPUT_STYLISH_NESTED),
        (JSON_FLAT_FL1, JSON_FLAT_FL2, FORMATTERS[1], OUTPUT_PLAIN_FLAT),
        (YAML_FLAT_FL1, YAML_FLAT_FL2, FORMATTERS[1], OUTPUT_PLAIN_FLAT),
        (YML_FLAT_FL1, YML_FLAT_FL2, FORMATTERS[1], OUTPUT_PLAIN_FLAT),
        (JSON_TREE_FL1, JSON_TREE_FL2, FORMATTERS[1], OUTPUT_PLAIN_NESTED),
        (YAML_TREE_FL1, YAML_TREE_FL2, FORMATTERS[1], OUTPUT_PLAIN_NESTED),
        (YML_TREE_FL1, YML_TREE_FL2, FORMATTERS[1], OUTPUT_PLAIN_NESTED),
        (JSON_FLAT_FL1, JSON_FLAT_FL2, FORMATTERS[2], OUTPUT_JSON_FLAT),
        (YAML_FLAT_FL1, YAML_FLAT_FL2, FORMATTERS[2], OUTPUT_JSON_FLAT),
        (YML_FLAT_FL1, YML_FLAT_FL2, FORMATTERS[2], OUTPUT_JSON_FLAT),
        (JSON_TREE_FL1, JSON_TREE_FL2, FORMATTERS[2], OUTPUT_JSON_NESTED),
        (YAML_TREE_FL1, YAML_TREE_FL2, FORMATTERS[2], OUTPUT_JSON_NESTED),
        (YML_TREE_FL1, YML_TREE_FL2, FORMATTERS[2], OUTPUT_JSON_NESTED),
    ),
)
def test_generate_diff(argument1, argument2, formatter, expected):
    with open(expected) as result_file:
        expected_result = result_file.read()
        assert generate_diff(
            argument1, argument2, formatter
        ) == expected_result
