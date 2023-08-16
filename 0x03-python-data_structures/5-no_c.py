#!/usr/bin/pytthon3
def no_c(my_string):
    translate_char = str.maketrans('', '', 'cC')
    new_string = my_string.translate(translate_char)
    return new_string
