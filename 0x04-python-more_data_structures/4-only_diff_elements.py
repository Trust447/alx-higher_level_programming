#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    difference = []
    for item in set_1:
        if item not in set_2:
            difference.append(item)
    for items in set_2:
        if items not in set_1:
            difference.append(items)
    return difference
