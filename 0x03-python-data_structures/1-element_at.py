#!/usr/bin/python3
def element_at(my_list, idx):
    """
    my_list: a list
    @idx: index of element
    Return: element of list
    """
    if (idx < 0) or (idx > len(my_list) - 1):
        return None
    else:
        return my_list[idx]
