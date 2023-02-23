from pathlib import Path
import json
import yaml


def load_file(*args):
    path = Path(*args)
    with open(path) as file:
        if path.suffix == '.json':
            return json.load(file)
        elif path.suffix == '.yaml' or '.yml':
            return yaml.safe_load(file)
        else:
            return file.read()
