#!/usr/bin/env python3
# coding=utf-8

"""
Function for Factorial Numbers
It will Return the Factorial in loop
"""

def factorial(num:int)->int:
    retval=1
    while num>1:
        retval=retval*num
        num=num-1
    return retval

