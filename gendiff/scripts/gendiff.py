#!/usr/bin/env python3
from gendiff.gendiff import generate_diff
from ..cli import parse_arguments


def main():
    args = parse_arguments()
    return generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
