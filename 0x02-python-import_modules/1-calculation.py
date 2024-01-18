#!/usr/bin/python3
#this line ensures that this script is executed when run directly not imported
if __name__ == "__main__":
    #import necessary functions from calculator_1 module
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    #executes arithmatic operations and displays it
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
    