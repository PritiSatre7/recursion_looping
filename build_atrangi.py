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

def build_atrangi(nterm: int) -> float:
    total = 0
    i = 1
    while i <= nterm:
        total = total + (i / atrangi(i))
        i += 1
    return total

if __name__ == "__main__":
    print(build_atrangi(5))


