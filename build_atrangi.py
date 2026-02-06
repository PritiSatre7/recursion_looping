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

def atarangi(nterm: int) -> int:
    """
    get value of atarangi series for a given term

    :param nterm:
    :return:
    """
    logger.debug("Function is called")
    if nterm == 0:
        logger.info("Base case")
        return 0
    elif nterm == 1 or nterm == 2:
        logger.info("Base case")
        return 1
    else:
        logger.debug("Calculation Start")
        return 2 * atarangi(nterm-1) - 3 * atarangi(nterm-2) + 4 * atarangi(nterm-3)


def build_atrangi(nterm: int) -> float:
    """
       This function calculates the series:
       1/1! + 2/2! + 3/3! + ... + n/n!
    """
    logger.info("Building atrangi series for nterm")
    total = 0
    i = 1
    while i <= nterm:
        total = total + (i / atarangi(i))
        logger.info(f"Term (i): (i)/(i)! = value, Total = total")
        i += 1
        logger.info("Final sum")
    return total

if __name__ == "__main__":
    logger.info("Program started")
    result = build_atrangi(5)
    logger.info("Program finished with result")
    print(build_atrangi(5))
    print(atarangi(4))


