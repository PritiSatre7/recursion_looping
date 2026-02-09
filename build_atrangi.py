#!/usr/bin/env python3
# coding=utf-8

"""
Function for Recurrence Atrangi
It will return a single integer value for given.
"""


import logging
import fibo
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def build_atrangi(nterm: int) -> float:
    """
    This function calculates the series:
    1/atrangi(1) + 2/atrangi(2) + 3/atrangi(3) + ...
    """
    logger.info("Building atrangi series")
    total = 0
    i = 1

    while i <= nterm:
        value = i / fibo.atarangi(i)   # using imported atrangi
        total += value
        logger.info(f"Term {i}: {i}/{i}! = {value}")
        i += 1

    logger.info("Final sum calculated")
    return total

if __name__ == "__main__":
    logger.info("Program started")

    result = build_atrangi(5)
    print("Series result:", result)

    print("atarangi(4):", fibo.atarangi(4))

    logger.info("Program finished")



