#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxi = max(list(a_dictionary.values()))
    top = [name for name in a_dictionary if a_dictionary[name] == maxi]
    return top
