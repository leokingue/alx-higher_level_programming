#!/usr/bin/python3
"""
5. Save Object to a file
"""

import json


def save_to_json_file(my_obj, filename):
    """Save a json object to file"""
    with open(filename, "w", encoding="utf-8") as new_fil:
        json.dump(my_obj, new_fil)
