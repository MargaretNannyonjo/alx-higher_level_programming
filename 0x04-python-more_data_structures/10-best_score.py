#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None  # Return None if the dictionary is empty or None

    best_key = None
    max_score = float('-inf')  # Set the initial max score to negative infinity

    # Iterate through the dictionary's key-value pairs
    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            best_key = key

    return best_key
