#!/usr/bin/python3
"""
Content of the append_write function
"""


def append_write(filename="", text=""):
    """append_write implementation"""
    with open(filename, "a", encoding="utf-8") as new_fil:
        len_text = len(text)
        new_fil.write(text)
        return len_text
