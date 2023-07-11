#!/usr/bin/prython3
"""
Defines a sript that adds all the arguments to a Python
list and save it to a JSON file
"""


import sys
import json

save_to_json_file = __import__('save_to_json_file').save_to_json_file
load_from_json_file = __import__('load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

for arg in sys.argv[1:]:
    items.append(arg)

save_to_json_file(items, filename)
