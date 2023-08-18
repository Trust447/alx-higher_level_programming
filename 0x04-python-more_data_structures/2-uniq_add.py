#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set()
    new_list = []
    for item in my_list:
        if item not in unique:
            unique.add(item)
            new_list.append(item)
    return new_list
