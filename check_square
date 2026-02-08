#!/usr/bin/env python3
# coding=utf-8

"""
Function for Square Progression
The function generates a string consisting only of opening parentheses '('.
"""

#!/usr/bin/env python3
# coding=utf-8

"""
Function for Square Progression
The function generates a string consisting only of opening parentheses '('.
"""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
    print(backfall(0))
    print(backfall(1))
    print(backfall(4))
    print(backfall(9))
    print(backfall(16))


