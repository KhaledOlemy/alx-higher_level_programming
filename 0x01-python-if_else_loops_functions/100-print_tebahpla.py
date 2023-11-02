#!/usr/bin/python3
char = 91
minus = -33
plus = 31
while char != 65:
    x = chr(char)
    if char >= 97:
        char += minus
    else:
        char += plus
    print("".format(chr(char)), end="")
