#!/usr/bin/python3
if _name_ == "_main_":
    import hidden_4
    # print sorted name from directory
    for name in sorted(dir(hidden_4)):
        # print only names that dont start with_
        if name[:2] != '_':
            print("{}".format(name))
