#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except (ValueError,ZeroDivisionError):
        return None
    finally:
        print("{}".format(result))
    return result
