#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for size in my_list:
        if my_list == []:
            return (my_list)
        elif idx > 0 or idx > size:
            del my_list[idx]
            return (my_list)
        else:
            return (my_list)