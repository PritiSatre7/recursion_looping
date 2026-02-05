#!/usr/bin/env python3
# coding=utf-8

"""
Function for Factorial Numbers
It will Return the Factorial in loop
"""

import logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

def factorial(num:int)->int:
    logger.info("Starting factorial calculation")

    retval=1
    while num>1:
        logger.debug("Multiplying retval with num")
        retval=retval*num
        num=num-1
        logger.info("Factorial calculation completed")
    return retval

if __name__ == "__main__":
    logger.info("Program started")
    print(factorial(5))
    logger.info("Program finished")