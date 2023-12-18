def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    index = 0

    try:
        while printed_integers < x:
            value = my_list[index]
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                printed_integers += 1
            index += 1
    except IndexError:
        pass

    print()
    return printed_integers
