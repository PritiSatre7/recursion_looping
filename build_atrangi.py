#!/usr/bin/env python3
# coding=utf-8

"""
Function for Recurrence Atrangi
It will return a single integer value for given.
"""

def atrangi(n: int) -> int:
    fact = 1
    while n > 0:
        fact = fact * n
        n -= 1
    return fact



