#!/usr/bin/env python3
# coding=utf-8

"""
Function for Quadrilateral Progressions
Return condition is True or False
"""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def is_quad(a:int, b:int, c:int, d:int )->bool:
    if a+b+c<=d:
        logger.debug("fourth side is <= the sum of first three")
        logger.info("Invalid quadrilateral")
        return False
    elif b+c+d<=a:
        logger.debug("fourth side is <= the sum of first three")
        logger.info("Invalid quadrilateral")
        return False
    elif c+d+a<=b:
        logger.debug("fourth side is <= the sum of first three")
        logger.info("Invalid quadrilateral")
        return False
    else:
        logger.info("Valid quadrilateral")
        return True

if __name__=="__main__":
    if not is_quad(1, 2, 3, 4):
        logger.warning("Invalid quadrilateral")
    else:
        logger.info("Valid quadrilateral")
