#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n').replace('?', '?\n\n').replace(':', ':\n\n')
    text = text.replace('.\n\n ', '.\n\n').replace('?\n\n ', '?\n\n').replace(':\n\n ', ':\n\n')
    text = text.replace(' .\n\n', '.\n\n').replace(' ?\n\n', '?\n\n').replace(' :\n\n', ':\n\n')
    print("{}".format(text), end="")
    if text[-1] != "\n":
        print('\n')
