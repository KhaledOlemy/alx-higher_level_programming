#!/usr/bin/python3
def uppercase(str):
    if str == "":
        print("\n", end="")
    for letter in range(len(str)):
        end = ""
        if letter == len(str) - 1:
            end = "\n"
        temp = str[letter]
        if 122 >= ord(temp) >= 97:
            temp = chr(ord(str[letter]) - 32)
        print("{}".format(temp), end=end)
