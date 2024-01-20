#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        if sys.argv[2] == '+':
            result = add(int(sys.argv[1]), int(sys.argv[3]))
            print("{} + {} = {}".format(sys.argv[1], sys.argv[3], result))
        elif sys.argv[2] == '-':
            result = sub(int(sys.argv[1]), int(sys.argv[3]))
            print("{} - {} = {}".format(sys.argv[1], sys.argv[3], result))
        elif sys.argv[2] == '*':
            result = mul(int(sys.argv[1]), int(sys.argv[3]))
            print("{} * {} = {}".format(sys.argv[1], sys.argv[3], result))
        else:
            result = div(int(sys.argv[1]), int(sys.argv[3]))
            print("{} / {} = {}".format(sys.argv[1], sys.argv[3], result))
