#!/usr/bin/env python3
# coding=utf-8

"""
Function for Quadrilateral Progressions
Return condition is True or False
"""

def is_quad(a:int, b:int, c:int, d:int )->bool:
    if a+b+c+<=d:
        return False
    elif b+c+d<=a:
        return False
    elif c+d+a<=b:
        return False
    else:
        return True
