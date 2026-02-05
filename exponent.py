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
        return num*pow (num,pow-1)
    