#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# 使用递归函数需要注意防止栈溢出。

# 尾递归优化

def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
