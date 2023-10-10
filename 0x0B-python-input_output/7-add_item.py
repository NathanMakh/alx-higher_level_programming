#!/usr/bin/python3
import sys
import json

# Function to save a Python object to a JSON file
def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)

# Function to load a Python object from a JSON file
def load_from_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# Check if the file exists, and load its content if it does
try:
    existing_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    existing_list = []

# Add command-line arguments to the list
existing_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(existing_list, 'add_item.json')
