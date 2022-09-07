#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        char = str[i]
        if str[i] >= 'a' and str[i] <= 'z':
            char = chr(ord(str[i]) - 32)
        print("{}".format(char), end="")
    print()
