#!/usr/bin/env python3
# coding=utf-8

"""
Function for Recurrence Atrangi
It will return a single integer value for given.
"""
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def atrangi(n: int) -> int:
    logger.info("Calculating factoraial")
    fact = 1
    while n > 0:
        fact = fact * n
        logger.debug("Fact updated ")
        n -= 1
        logger.info("Factorial result")
    return fact

def build_atrangi(nterm: int) -> float:
    logger.info("Building atrangi series for nterm")
    total = 0
    i = 1
    while i <= nterm:
        total = total + (i / atrangi(i))
        logger.info(f"Term (i): (i)/(i)! = value, Total = total")
        i += 1
        logger.info("Final sum")
    return total

if __name__ == "__main__":
    logger.info("Program started")
    result = build_atrangi(5)
    logger.info("Program finished with result")
    print(build_atrangi(5))


