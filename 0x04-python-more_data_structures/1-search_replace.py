#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def serch_element(element):
        return element if search != element else replace
    return list(map(search_element, my_list))
