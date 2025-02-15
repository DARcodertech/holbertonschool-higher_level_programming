#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, 'r') as f:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
        json_data = json.dumps(data, indent=4)
        with open('data.json', 'w') as f:
            json_.file.wrie(json_data)
        return True
    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except Exception as r:
        print(f"An error occurred: {str(r)}")
        return False
