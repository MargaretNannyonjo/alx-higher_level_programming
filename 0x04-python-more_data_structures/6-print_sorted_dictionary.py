#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort the keys of the dictionary in alphabetical order
    sorted_keys = sorted(a_dictionary.keys())

    # Print the key-value pairs in the sorted order
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
