import math

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def atarangi(nterm: int) -> int:
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



if __name__ == "__main__":
    print(atarangi(4))




