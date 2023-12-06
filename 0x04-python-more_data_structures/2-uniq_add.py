#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set()
    total = 0

    # Iterate through each element in the list
    for num in my_list:
        # Add unique elements to the set and sum them up
        if num not in unique_numbers:
            unique_numbers.add(num)
            total += num

    return total
