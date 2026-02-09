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

if __name__ == "__main__":
    print(perfect_square_iter("(", 16))
