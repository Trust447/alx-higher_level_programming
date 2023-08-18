#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set()
    count = 0
    for item in my_list:
        if item not in unique:
            unique.add(item)
            count += item
    return count
