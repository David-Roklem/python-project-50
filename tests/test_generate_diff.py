import pytest
from gendiff.gendiff import generate_diff
from pathlib import Path


@pytest.mark.parametrize('file1, file2, expected', [
    (Path('tests', 'fixtures', 'file1.json'), 
     Path('tests', 'fixtures', 'file2.json'),
     Path('tests', 'fixtures', 'result.txt')),
    (Path('tests', 'fixtures', 'file1.yaml'), 
     Path('tests', 'fixtures', 'file2.yaml'),
     Path('tests', 'fixtures', 'result.txt'))
    ])
def test_generate_diff(file1, file2, expected):
    diff = generate_diff(file1, file2)
    assert diff == expected.read_text()
