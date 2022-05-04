#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def power1(x):
    return x * x


def power2(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def power3(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
