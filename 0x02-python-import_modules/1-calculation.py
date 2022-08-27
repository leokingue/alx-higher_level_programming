#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 1
    b = 2
    printf("{} + {} = {}".format(a, b, add(a, b)))
    printf("{} + {} = {}".format(a, b, sub(a, b)))
    printf("{} + {} = {}".format(a, b, mul(a, b)))
    printf("{} + {} = {}".format(a, b, div(a, b)))
