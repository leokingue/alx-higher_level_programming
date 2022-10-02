#!/usr/bin/python3
"""
Contents of the read_file definition
"""


def read_file(filename=""):
    """Read file function"""
    with open(filename, "r", encoding="utf-8") as new_fil:
        print(new_fil.read(), end="")
