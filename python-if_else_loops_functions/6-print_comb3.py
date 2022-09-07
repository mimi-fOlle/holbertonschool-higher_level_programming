#!/usr/bin/python3
for nmb1 in range(0, 9):
    for nmb2 in range(nmb1 + 1, 10):
        if nmb1 == 8 and nmb2 == 9:
            print("{}{}\n".format(nmb1, nmb2), end="")
        elif nmb2 != nmb1:
            print("{}{}".format(nmb1, nmb2), end=", ")
