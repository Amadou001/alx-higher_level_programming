#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            upper_case = ord(x) - 32
            print("{:c}".format(upper_case), end=' ')
        else:
            print("{}".format(x), end='')
    print()  
