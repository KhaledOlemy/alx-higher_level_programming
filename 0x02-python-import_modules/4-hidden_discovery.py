#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for name in names:
        case1 = 90 >= ord(name[0]) >= 65
        case2 = 122 >= ord(name[0]) >= 97
        cases = case1 or case2
        if name[:2] != "__" and cases:
            print(name)
