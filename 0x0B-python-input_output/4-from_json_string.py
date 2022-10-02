#!/usr/bin/python3
"""
Contain  From JSON string to Object
"""

import json


def from_json_string(my_str):
    """Return object from json"""
    return json.loads(my_str)
