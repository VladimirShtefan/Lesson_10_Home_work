from json import load


def load_json(file_name: str) -> list:
    with open(file_name) as file:
        data = load(file)
    return data
