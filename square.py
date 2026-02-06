#!/usr/bin/env python3
# coding=utf-8

"""
Function for Square
It will Return True if condition is satisfied else False
"""

def is_square(a:int, b:int,c:int, d:int) -> bool:
    if is_rectangle(a, b, c, d)is False:
        return False
    if a!=b:
        return False
    if c!=d:
        return False
    else:
        return True

if __name__ == "__main__":
    print(is_square(1,2,3,4))

