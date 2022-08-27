#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    printf("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    printf("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    printf("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    printf("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
