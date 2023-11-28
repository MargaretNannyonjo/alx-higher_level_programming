#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Description: Prints the last digit of a number
if number >= 0:
    last_digit_original = number % 10
else:
    last_digit_original = -(-number % 10)
if last_digit_original > 5:
    print(
         "Last digit of",
         number,
         "is", last_digit_original,
         "and is greater than 5"
         )
elif last_digit_original == 0:
    print(
         "Last digit of",
         number,
         "is", last_digit_original,
         "and is 0"
         )
else:
    print(
         "Last digit of",
         number,
         "is", last_digit_original,
         "and is less than 6 and not 0"
         )
