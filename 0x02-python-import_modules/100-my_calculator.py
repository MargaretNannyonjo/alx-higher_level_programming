#!/usr/bin/python3
if _name_ == "_main_":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv)
    if arg != 4:
        print("Usage:{}<a> <operator> <b>".format(argv[0]))
        exit(1)
        ops = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div
            }
        if argv[2] in ops:
            num1 = int(argv[1])
            num2 = int(argv[3]
            op = ops[argv[2]]
            result = op(num1, num2)
              print("{:d} {:s} {:d} = {:d}".format(num1, argv[2], num2, result))
        else:
            print("Unknown operator. Available operators: +, -, *, and /")
            exit(1)
            exit(0)
