#!/usr/bin/python3
# Printing all possible combinations of two different digits
for i in range(10):
    for j in range(i + 1, 10):
        print("{:d}{:d}".format(i, j), end=", " if i != 8 or j != 9 else "\n")
