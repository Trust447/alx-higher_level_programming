#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        if search < len(my_list):
            my_list[search] = replace
    return my_list[search]
