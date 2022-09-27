#!/usr/bin/python3
""" Module: 7-add_item """


import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(args, filename):
    my_list = []
    filename = "add_item.json"

    my_list = load_from_json_file(filename)

    for i in args:
        my_list.append(i)
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    add_item(args, filename)
