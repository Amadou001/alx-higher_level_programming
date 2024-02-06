#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        message = "Exception: Unable to print the value as an integer"
        sys.stderr.write(message + '\n')
        return False
