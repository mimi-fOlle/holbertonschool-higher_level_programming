#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    for idx, element in enumerate(new):
        if element == search:
            new[idx] = replace
    return (new)
