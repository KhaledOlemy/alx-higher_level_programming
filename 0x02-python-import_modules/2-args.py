#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("{} argument:".format(1))
    else:
        print("{} arguments:".format(len(argv) - 1))
    for i in range(len(argv)-1):
        print("{}: {}".format(i + 1, argv[i+1]))
