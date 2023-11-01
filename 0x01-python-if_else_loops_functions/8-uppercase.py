#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        end = ""
        if 122 >= ord(letter) >= 97:
            letter = chr(ord(letter) - 32)
        if letter == str[-1]:
            end = "\n\n"
        print("{}{}".format(letter, end), end="")
