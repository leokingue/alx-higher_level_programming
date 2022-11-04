#!/usr/bin/python3
"""
module Base
"""


class Base:
    """Implementation Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor of Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
