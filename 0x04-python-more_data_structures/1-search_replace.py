#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []

    # Iterate through each element in the original list
    for element in my_list:
        if element == search:
            new_list.append(replace)  # Replace with the new element
        else:
            new_list.append(element)

    return new_list
