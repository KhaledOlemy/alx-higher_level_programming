#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxi = min(my_list)
    for num in my_list:
        if num > maxi:
            maxi = num
    return (maxi)
