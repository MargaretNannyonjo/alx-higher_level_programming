#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    size = len(args)

    if size > 1:
        print("{} arguments:".format(size))
        for i, arg in enumerate(args, 1):
            print("{}: {}".format(i, arg))
    elif size == 0:
        print("{} arguments:".format(size))
    else:
        print("{}: {}".format(size, args[0]))
