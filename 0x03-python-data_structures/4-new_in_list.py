#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        my_list_copy = my_list.copy()
        if (0 > idx) or (idx >= len(my_list)):
            return my_list_copy
        else:
            my_list[idx] = element
            return my_list
