#!/usr/bin/python3
"""Reads the code"""

from sys import stdin


try:
    my_dict = {}
    total_size = 0
    for i, line in enumerate(stdin, start=1):
        line = line.strip()
        parts = line.split(" ")
        total_size += int(parts[-1])
        if parts[-2] not in my_dict:
            my_dict[parts[-2]] = 1
        else:
            my_dict[parts[-2]] += 1
        my_dict = dict(sorted(my_dict.items()))
        if i % 10 == 0:
            print("File size: {}".format(total_size))
            for key, val in my_dict.items():
                print("{}: {}".format(key, val))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for key, val in my_dict.items():
        print("{}: {}".format(key, val))
