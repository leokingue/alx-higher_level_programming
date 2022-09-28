#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """My own class list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Method that displays the sorted elements"""
        print(sorted(self))
