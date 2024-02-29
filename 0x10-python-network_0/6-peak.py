#!/usr/bin/python3
# find the peak
def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    if len(set(list_of_integers)) == 1:
        return list_of_integers[0]
    old_peak = list_of_integers[0]
    peak = list_of_integers[0]
    ascending = None
    descending = None
    for i in range(len(list_of_integers)):
        for j in range(i, len(list_of_integers)):
            if j == len(list_of_integers):
                return peak
            if list_of_integers[j+1] > list_of_integers[j]:
                ascending = True
                descending = None
            elif list_of_integers[j+1] < list_of_integers[j] and ascending:
                return peak
            elif list_of_integers[j+1] < list_of_integers[j]:
                ascending = None
                descending = True
            if ascending:
                peak = list_of_integers[j+1]
            elif descending:
                pass
            if list_of_integers[j+1] == list_of_integers[j]:
                return old_peak
    return peak
