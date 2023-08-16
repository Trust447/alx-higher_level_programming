#!/usr/bin/pytthon3
def no_c(my_string):
    for char in my_string:
        if char == 'c':
            my_string.translate({ord('c'): None})
        if char == 'C':
            my_string.translate({ord('C'): None})
             
    return my_string
