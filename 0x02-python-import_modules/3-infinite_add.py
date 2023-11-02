#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    output = 0
    if len(argv) == 1:
        print("{}".format(0))
    else:
        for i in range(len(argv)-1):
            output += int(argv[i+1])
        print("{}".format(output))
