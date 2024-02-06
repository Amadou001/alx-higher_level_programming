#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except( TypeError, ValueError):
        message = "Exception: Unknown format code 'd' for object of type 'str'"
        sys.stderr.write(message + '\n')
        return False