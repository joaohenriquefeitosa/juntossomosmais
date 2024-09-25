import json

def parse_json(file_path: str) -> dict:
    """Parse a JSON file and return a dictionary."""
    
    with open(file_path, mode='r', encoding='utf-8') as file:
        return json.load(file)