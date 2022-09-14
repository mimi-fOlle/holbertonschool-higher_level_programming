#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = [*set(my_list)]
    sum = 0
    for i in range(0, len(res)):
        sum += res[i]
    return (sum)
