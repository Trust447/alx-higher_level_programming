#!/usr/bin/python3
"""module that Write a script that adds all arguments
to a Python list, and then save them to a file"""
import sys
import os
save_to_j = __import__(5-save_to_json_file).save_to_json_file
load_from_j =  __import__(6-load_from_json_file).load_from_json_file



my_list = []

if os.path.exist(add_item.json):
    my_list = load_from_j(add_item.json)
else:
    my_list = []
for args in sys.argv[1:]:
    my_list.append(args)

save_to_j(my_list, add_item.json)
