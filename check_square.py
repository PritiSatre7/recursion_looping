"""
Perfect square

Function checks if the input is a perfect square, if not it falls back to the previous perfect square.

"""

import logging
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

if __name__ == "__main__":
    print(perfect_square(0))
    print(perfect_square(1))
    print(perfect_square(4))
    print(perfect_square(9))
    print(perfect_square(16))
    print(perfect_square(-16))
