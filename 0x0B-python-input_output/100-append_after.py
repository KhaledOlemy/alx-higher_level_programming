#!/usr/bin/python3
"""APPEND AFTER SEARCG TERM"""


def append_after(filename="", search_string="", new_string=""):
    """append after"""
    with open(filename, "r", encoding="UTF-8") as f:
        listie = f.read().split('\n')
    for i in range(len(listie)):
        if i == len(listie) - 1:
            continue
        listie[i] = listie[i] + '\n'
    for i in range(len(listie)):
        if search_string in listie[i]:
            listie[i] = listie[i] + new_string
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(''.join(listie))
