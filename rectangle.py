#!/usr/bin/env python3
# coding=utf-8

"""
Function for Rectangle
It will Return True if condition is satisfied else False
"""


def is_rectangle(a:int, b:int, c:int, d:int)->bool:
    if a*a + b*b!= b*b + c*c:
        return False
    else:
        return True

if __name__ == "__main__":
    print(is_rectangle(3,4,5,6))