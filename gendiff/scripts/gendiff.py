#!/usr/bin/env python3
from gendiff.gendiff import generate_diff
from ..cli import parse_arguments


def main():
    """Run generate_diff."""
    args = parse_arguments()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
