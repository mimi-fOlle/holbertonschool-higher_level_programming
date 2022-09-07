#!/usr/bin/python3
for nmb in range(0, 100):
    if nmb == 99:
        print(f"{nmb:02}")
    else:
        print(f"{nmb:02}", end=", ")
