#!/usr/bin/python3
for nmb in range(0, 100):
    if nmb == 99:
        print("{:02d}".format(nmb))
    else:
        print("{:02d}".format(nmb), end=", ")
