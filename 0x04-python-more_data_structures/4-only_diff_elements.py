#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    x = list(set_1)
    y = list(set_2)
    x.extend(y)
    return list(set([i for i in x if x.count(i) == 1]))
