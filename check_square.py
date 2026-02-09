#!/usr/bin/env python3
# coding=utf-8

"""
Perfect square
Function will create a strings and a series based on perfect squares and it will fall back to the previous square when needed.
"""


import math

def perfect_square_iter(ch: str, n: int) -> str:
    if n <= 0:
        return ""
    root = math.isqrt(n)

    if root == 0:
        return ""
    return ch + perfect_square_iter(ch, (root - 1) * (root - 1))


if __name__ == "__main__":
    print(perfect_square_iter(".", 0))
    print(perfect_square_iter(".", 1))
    print(perfect_square_iter("(", 4))
    print(perfect_square_iter("(", 9))
    print(perfect_square_iter("x", 16))
