#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    # print sorted name from directory
    for name in sorted(dir(hidden_4)):
        # print only names that don't start with _
        if name[:1] != '_':
            print("{}".format(name))
