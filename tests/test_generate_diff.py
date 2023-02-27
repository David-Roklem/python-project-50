# import pytest
# import gendiff.file_reader
# from gendiff.gendiff import generate_diff
# from gendiff.formatters.formats import JSON, STYLISH, PLAIN


# FLAT_JSON_FILE1 = 'tests/fixtures/file1.json'
# FLAT_JSON_FILE2 = 'tests/fixtures/file2.json'
# FLAT_YAML_FILE1 = 'tests/fixtures/file1.yaml'
# FLAT_YAML_FILE2 = 'tests/fixtures/file2.yaml'
# FLAT_YML_FILE1 = 'tests/fixtures/file1.yml'
# FLAT_YML_FILE2 = 'tests/fixtures/file2.yml'
# NESTED_JSON_FILE1 = 'tests/fixtures/file1_nested.json'
# NESTED_JSON_FILE2 = 'tests/fixtures/file2_nested.json'
# NESTED_YAML_FILE1 = 'tests/fixtures/file1_nested.yaml'
# NESTED_YAML_FILE2 = 'tests/fixtures/file2_nested.yaml'

# ANSWER_STYLISH_FLAT = 'tests/fixtures/answer_stylish_flat'
# ANSWER_STYLISH_NESTED = 'tests/fixtures/answer_stylish_nested'
# ANSWER_PLAIN_FLAT = 'tests/fixtures/answer_plain_flat'
# ANSWER_PLAIN_NESTED = 'tests/fixtures/answer_plain_nested'
# ANSWER_JSON_FLAT = 'tests/fixtures/answer_json_flat'
# ANSWER_JSON_NESTED = 'tests/fixtures/answer_json_nested'


# def get_answer(answer_path):
#     return gendiff.file_reader.read_data(answer_path)


# @pytest.mark.parametrize('filepath1, filepath2, format_name, answer', [
#     (FLAT_JSON_FILE1, FLAT_JSON_FILE2, STYLISH, ANSWER_STYLISH_FLAT),
#     (FLAT_YAML_FILE1, FLAT_YAML_FILE2, STYLISH, ANSWER_STYLISH_FLAT),
#     (FLAT_YML_FILE1, FLAT_YML_FILE2, STYLISH, ANSWER_STYLISH_FLAT),
#     (NESTED_JSON_FILE1, NESTED_JSON_FILE2, STYLISH, ANSWER_STYLISH_NESTED),
#     (NESTED_YAML_FILE1, NESTED_YAML_FILE2, STYLISH, ANSWER_STYLISH_NESTED),
#     (FLAT_JSON_FILE1, FLAT_JSON_FILE2, PLAIN, ANSWER_PLAIN_FLAT),
#     (FLAT_YAML_FILE1, FLAT_YAML_FILE2, PLAIN, ANSWER_PLAIN_FLAT),
#     (FLAT_YML_FILE1, FLAT_YML_FILE2, PLAIN, ANSWER_PLAIN_FLAT),
#     (NESTED_JSON_FILE1, NESTED_JSON_FILE2, PLAIN, ANSWER_PLAIN_NESTED),
#     (NESTED_YAML_FILE1, NESTED_YAML_FILE2, PLAIN, ANSWER_PLAIN_NESTED),
#     (FLAT_JSON_FILE1, FLAT_JSON_FILE2, JSON, ANSWER_JSON_FLAT),
#     (FLAT_YAML_FILE1, FLAT_YAML_FILE2, JSON, ANSWER_JSON_FLAT),
#     (FLAT_YML_FILE1, FLAT_YML_FILE2, JSON, ANSWER_JSON_FLAT),
#     (NESTED_JSON_FILE1, NESTED_JSON_FILE2, JSON, ANSWER_JSON_NESTED),
#     (NESTED_YAML_FILE1, NESTED_YAML_FILE2, JSON, ANSWER_JSON_NESTED),
# ])
# def test_generate_diff(filepath1, filepath2, format_name, answer):
#     answer = get_answer(answer)
#     l_answer = len(answer)  # length answer
#     assert generate_diff(
#         filepath1, filepath2, format_name
#     ) == answer[:l_answer - 1]
