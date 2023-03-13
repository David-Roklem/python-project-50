# Gendiff

### Hexlet tests and linter status:
[![Actions Status](https://github.com/David-Roklem/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/David-Roklem/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/81b3b34e95e211a425a3/maintainability)](https://codeclimate.com/github/David-Roklem/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/81b3b34e95e211a425a3/test_coverage)](https://codeclimate.com/github/David-Roklem/python-project-50/test_coverage)
***

### A package for comparing two json/yaml files
Files can be mixed (ex., one file is json, another one is yaml)
There are three provided outputs:
- **stylish** (set by default)
- **plain**
- **json**
***

### Installation guide
```
git clone https://github.com/David-Roklem/python-project-50.git
cd python-project-50
make install
```
***

### Help command
```
gendiff -h

usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f {json,stylish,plain}, --format {json,stylish,plain}
                        output format (default: stylish)
```
***

### Output
There are test files you can use for experimenting with output. 
For instance, use the following command:
```gendiff tests/fixtures/file1.yaml tests/fixtures/file2.json```
The output will be:
```
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```
If you slightly alter the command adding plain option:
```gendiff -f plain tests/fixtures/file1.yaml tests/fixtures/file2.json```
You will get:
```
Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true
```
***

### asciinema

Help output
[![asciicast](https://asciinema.org/a/562163.svg)](https://asciinema.org/a/562163)

Finding difference between two json and yaml files (stylish)
[![asciicast](https://asciinema.org/a/VxyukEoVqmJuVNdtM968lVjKG.svg)](https://asciinema.org/a/VxyukEoVqmJuVNdtM968lVjKG)

Recursively finding difference between two json and yaml files (stylish)
[![asciicast](https://asciinema.org/a/pGhfzGViE9Abn2uJGFk8KTIRN.svg)](https://asciinema.org/a/pGhfzGViE9Abn2uJGFk8KTIRN)

Finding difference between two json and yaml files (plain)
[![asciicast](https://asciinema.org/a/u5d6g8QGCTcPn9qlrhPPsubAB.svg)](https://asciinema.org/a/u5d6g8QGCTcPn9qlrhPPsubAB)

Finding difference between two json and yaml files (flat)
[![asciicast](https://asciinema.org/a/ehi8MgUkYUNJudUQ2UUYpGs3z.svg)](https://asciinema.org/a/ehi8MgUkYUNJudUQ2UUYpGs3z)