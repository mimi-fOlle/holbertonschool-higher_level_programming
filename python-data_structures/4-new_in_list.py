#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = list(my_list)
    if idx in range(len(my_list)):
        my_list[idx] = element
    return (copy_list)
