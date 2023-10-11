#!/usr/bin/python3
"""module that Write a script that adds all arguments
to a Python list, and then save them to a file"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file =  __import__('6-load_from_json_file').load_from_json_file
from os.path import exists



my_file = 'add_item.json'

if exists(my_file):
    my_list = load_from_json_file(my_file)
else:
    my_list = []
for args in sys.argv[1:]:
    my_list.append(args)

save_to_json_file(my_list, my_file)
