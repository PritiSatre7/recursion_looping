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

def perfect_square(num:int) -> int:
    logger.info("function started")
    if num < 0:
        logger.warning("Num is negative, return empty string")
        return " "
    i = 0
    while i * i <= num:
        logger.debug("checking next square")
        i = i + 1
    if i * i > num:
        logger.debug("Go one step back")
        i = i - 1
        logger.info("Returning dot as result")
    return "." * i


def backfall(n: int) -> str:
    """
    Returns a string of '(' characters based on square root logic.
    """
    logger.info("backfall called with n")

    if n <= 0:
        logger.info("n is less than or equal to 0, returning empty string")
        return ""

    root = int(n ** 0.5)
    logger.info("calculated square root value")

    result = "(" * root
    logger.info("returning result ")

    return result

if __name__ == "__main__":
    print(perfect_square(0))
    print(perfect_square(1))
    print(perfect_square(4))
    print(perfect_square(9))
    print(perfect_square(16))
    print(perfect_square(16))

    print(backfall(0))
    print(backfall(1))
    print(backfall(4))
    print(backfall(9))
    print(backfall(16))


