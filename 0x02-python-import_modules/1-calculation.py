#!/usr/bin/python3
from calculator_1 import add, sub, ml, div
if __name__ == "__main__":
    a = 10
    b = 5
    printf("{} + {} = {}".format(a, b, add(a, b)))
    printf("{} - {} = {}".format(a, b, sub(a, b)))
    printf("{} * {} = {}".format(a, b, mul(a, b)))
    printf("{} / {} = {}".format(a, b, div(a, b)))
