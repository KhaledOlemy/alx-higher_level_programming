#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    numero = number % 10
    print("{}".format(numero), end="")
    return (numero)
