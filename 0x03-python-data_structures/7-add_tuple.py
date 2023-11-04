#!/usr/bin/python3
def if_not_ret_zero(tuple_i=(), idx=0):
    if idx < 0 or idx > len(tuple_i) - 1:
        return 0
    return tuple_i[idx]


def add_tuple(tuple_a=(), tuple_b=()):
    num_1 = if_not_ret_zero(tuple_a, 0) + if_not_ret_zero(tuple_b, 0)
    num_2 = if_not_ret_zero(tuple_a, 1) + if_not_ret_zero(tuple_b, 1)
    return num_1, num_2
