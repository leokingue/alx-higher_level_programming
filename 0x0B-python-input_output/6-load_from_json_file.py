#!/usr/bin/python3
"""
Create object from a JSON file
"""


import json


def load_from_json_file(filename):
    """load from json file function"""
    with open(filename, "r", encoding="utf-8") as new_fil:
        json.load(new_fil)
