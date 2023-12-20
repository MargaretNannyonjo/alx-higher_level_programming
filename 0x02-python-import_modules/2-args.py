#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    size = len(args)

    if size > 1:
        print("{} arguments:".format(size))
        for i, arg in enumerate(args, 1):
            print("{}: {}".format(i, arg))
    elif size == 1:
        print("{} argument:".format(size))
        print("1: {}".format(args[0]))
    else:
        print("0 arguments.")
