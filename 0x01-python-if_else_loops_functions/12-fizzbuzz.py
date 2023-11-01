#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i//5 == i/5 and i//3 == i/3:
            var = "FizzBuzz"
        elif i//5 == i/5:
            var = "Buzz"
        elif i//3 == i/3:
            var = "Fizz"
        else:
            var = str(i)
        print("{}".format(var), end=" ")
