#!/usr/bin/env python3
# coding=utf-8

"""
Perfect square
Function will create a strings and a series based on perfect squares and it will fall back to the previous square when needed.
"""

import logging
import math

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def perfect_square_iter(ch: str, n: int) -> str:
    logger.debug("perfect_square_iter having input as character and interger and output as string")
    if n <= 0:
        logger.debug("n is less than or equal to 0, returning empty string")
        return ""

    root = math.isqrt(n)  #integer square root
    logger.debug(f"integer square root calculated: {root}")

    return ch * root


def calculate_y_series(nterm: int) -> str:
    """
    This function generates the series using while loop.
    it takes the number of terms as input and returns the series as a string.


    :param nterm:number of terms to generate series.
    :returns: A string representing generated series.

    """
    retval = ""
    i = 0
    while i <= nterm:
        if i == 0:
            retval += perfect_square_iter("", i) + perfect_square_iter("", i)
        else:
            retval += "-" * i
            retval += perfect_square_iter(".", i) + perfect_square_iter("(", i)

        i = i + 1

    return retval

if __name__ == "__main__":
    print(perfect_square_iter(".", 0))
    print(perfect_square_iter(".", 1))
    print(perfect_square_iter("(", 4))
    print(perfect_square_iter("(", 9))
    print(perfect_square_iter("x", 16))

    print(calculate_y_series(9))

