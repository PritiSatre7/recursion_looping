#!/usr/bin/env python3
# coding=utf-8

"""
Function for Exponentional Progressions
It will return the retval of num and power
"""

def power(num:int ,pow:int)->int:
    if pow == 0:
        return 1
    elif pow == 1:
        return num
    else:
        return num * power(num, pow-1)

def loop_pow(num:int,pow:int)->int:
    retval = 1
    while pow > 0:
        retval= num * retval
        pow = pow - 1
    return retval

if __name__ == "__main__":
    print(power(2,3))