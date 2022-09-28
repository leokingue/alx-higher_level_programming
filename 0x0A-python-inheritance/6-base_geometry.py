#!/usr/bin/python3
"""
BaseGeometry class implementation
"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
