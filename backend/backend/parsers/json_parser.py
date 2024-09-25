import json

def parse_json(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        return json.load(file)