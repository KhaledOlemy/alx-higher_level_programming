#!/usr/bin/python3
char = 97
while char <= ord('z'):
    if char != ord('e') and char != ord('q'):
        print("{}".format(chr(char)), end="")
    char += 1
