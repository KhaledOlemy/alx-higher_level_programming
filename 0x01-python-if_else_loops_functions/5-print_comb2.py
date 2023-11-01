#!/usr/bin/python3
i = 0
while i < 100:
    beg = ""
    if i < 10:
        beg = "0"
    if i == 99:
        end = "\n"
    else:
        end = ", "
    print("{}{}".format(beg, i), end=end)
    i += 1
