#!/usr/bin/python3
""" find the peak function """


def find_peak(list_of_integers):
    """
    find_peak: find the peak of the list
    input: list
    return: int
    """
    if not list_of_integers:
        return None
    if len(list_of_integers) <= 2 or max(list_of_integers) == min(list_of_integers):
        return max(list_of_integers)
    midPoint = len(list_of_integers) // 2
    condition_1 = list_of_integers[midPoint] >= list_of_integers[midPoint - 1]
    condition_2 = list_of_integers[midPoint] >= list_of_integers[midPoint + 1]
    if condition_1 and condition_2:
        return list_of_integers[midPoint]
    if midPoint > 0 and not condition_2:
        return find_peak(list_of_integers[midPoint:])
    if midPoint > 0 and not condition_1:
        return find_peak(list_of_integers[:midPoint])
