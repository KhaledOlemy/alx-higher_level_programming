#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    out = []
    for i in range(list_length):
        try:
            num = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            num = 0
        except TypeError:
            print("wrong type")
            num = 0
        except IndexError:
            print("out of range")
            num = 0
        finally:
            out.append(num)
    return out
