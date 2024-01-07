#!/usr/bin/python3
grades = int(input(Enter marks: ))
if grades >= 90:
    print("A")
elif grades >= 80 and grades <= 89:
    print("B")
elif grades >= 70 and grades <= 79:
    print("C")
elif grades >= 60 and grades <= 69:
    print("D")
elif grades < 60:
    print("F")
