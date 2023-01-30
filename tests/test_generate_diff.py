from gendiff.gendiff import generate_diff
import pytest
import files_opener


@pytest.mark.parametrize('file1, file2, expected', [
    ('fixtures.file1.json', 'fixtures.file2.json',
     files_opener.load_file('tests', 'fixtures', 'result.txt'))])#,
    # ('fixtures.file1.yml', 'fixtures.file2.yml',
    #  files_opener('tests', 'fixtures', 'result.txt'))])
def test_generate_diff(file1, file2, expected):
    diff = generate_diff(file1, file2)
    assert diff == expected