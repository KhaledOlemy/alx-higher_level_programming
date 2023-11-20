#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    if not roman_string:
        return 0
    convert = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    string = '|'.join(roman_string).split('|')
    out = 0
    rem = 0
    for i in range(len(string)):
        if i + 1 < len(string) and convert[string[i+1]] == convert[string[i]]:
            rem += convert[string[i]]
        elif i + 1 < len(string) and convert[string[i+1]] > convert[string[i]]:
            rem = 0 - rem - convert[string[i]]
        else:
            out = out + convert[string[i]] + rem
            rem = 0
    return out
