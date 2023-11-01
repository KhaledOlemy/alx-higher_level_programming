#!/usr/bin/python3
i = 0
while i < 100:
    if i / 11 == i // 11:
        i += 1
        continue
    beg = ""
    if i < 10:
        beg = "0"
    rem = i % 10
    div = i / 10
    if rem < div:
        i += 1
        continue
    end = ", "
    if i == 89:
        end = "\n"
    print("{}{}".format(beg, i), end=end)
    i += 1
