#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    out = 0
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end="")
            out += 1
        except IndexError:
            pass
    print("")
    return out
