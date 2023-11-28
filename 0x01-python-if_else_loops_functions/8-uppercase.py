#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Check if the character is lowercase
        if 'a' <= char <= 'z':
            # Convert the lowercase character to uppercase using ASCII values
            print(chr(ord(char) - 32), end='')
        else:
            print(char, end='')

    print()
