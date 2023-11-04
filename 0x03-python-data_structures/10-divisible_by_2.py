#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = list(my_list)
    for num in range(len(my_list)):
        if my_list[num] % 2 == 0:
            new_list[num] = True
        else:
            new_list[num] = False
    return new_list
