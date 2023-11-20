#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    out = 0
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end="")
            out += 1
        except (TypeError, ValueError):
            pass
    print("")
    return out
