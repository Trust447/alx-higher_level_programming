#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for items in range(len(my_list)):
        if my_list[items] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
