#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections.abc import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
for key in d:
    print(key)

# 默认情况下，dict迭代的是key。
# 如果要迭代value，可以用for value in d.values()
# 如果要同时迭代key和value，可以用for k, v in d.items()。

# 如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断：

print(isinstance('abc', Iterable), isinstance([1,2,3], Iterable), isinstance(123, Iterable))

# 如果要对list实现类似Java那样的下标循环

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
