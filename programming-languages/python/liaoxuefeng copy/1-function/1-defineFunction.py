#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


# empty function

def nop():
    pass


# pass
age = 20
if age >= 18:
    pass


# parm check

def my_abs_with_parm_check(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x


# return multi values

# return a tuple
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
