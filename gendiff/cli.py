import argparse
from .formatters import JSON, STYLISH, PLAIN


def parse_arguments():
    """Parse data from user.
    Returns:
         parser.parse_args()
    """
    parser = argparse.ArgumentParser(
        usage='gendiff [-h] [-f FORMAT] first_file second_file',
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        choices=[JSON, STYLISH, PLAIN],
        default='stylish',
        help='output format (default: %(default)s) ',
    )
    return parser.parse_args()
