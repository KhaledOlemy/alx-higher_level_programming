#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxi = [i for i in list(a_dictionary.values()) if i]
    if not maxi:
        return None
    maxi = max(maxi)
    top = [name for name in a_dictionary if a_dictionary[name] == maxi]
    return top[0]
