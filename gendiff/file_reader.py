"""Get format of file."""
from os.path import splitext


def get_format(filepath: str) -> str:
    """Get the file format.
    Parameters:
        filepath: path to the file.
    Returns:
        extension: string, with specified the file format
    """
    _, extension = splitext(filepath)
    if extension in ('.yaml', '.yml'):
        return 'yaml'
    elif extension == '.json':
        return 'json'
    raise TypeError(
        'Check the file(s) extension.\nOnly yaml, yml, or json '
        'file extensions are allowed.'
    )


def read_data(filepath: str):
    """Read the data from file.
    Parameters:
        filepath: path to the file.
    Returns:
        data: data from read file.
    """
    with open(filepath) as read_file:
        return read_file.read()
