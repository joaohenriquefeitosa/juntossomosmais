import csv

def parse_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        return [row for row in csv_reader]