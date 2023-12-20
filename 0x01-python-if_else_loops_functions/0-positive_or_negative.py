#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# Description: prints negative,zero or positive
if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")
