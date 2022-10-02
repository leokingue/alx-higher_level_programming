#!/usr/bin/python3
"""
Contents of the write_file definition
"""


def write_file(filename="", text=""):
    """Write file implementation"""
    with open(filename, "w", encoding="utf-8") as new_fil:
        return new_fil.write(text)
