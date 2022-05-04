#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

print(list(range(1, 11)))

print(
    [x * x for x in range(1, 11)],
    [x * x for x in range(1, 11) if x % 2 == 0],
    [m + n for m in 'ABC' for n in 'XYZ']
)

# 列出当前目录下的所有文件和目录名.
print([d for d in os.listdir('.')])

# 列表生成式可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

# list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# for前面的部分是一个表达式，它必须根据x计算出一个结果
print([x if x % 2 == 0 else -x for x in range(1, 11)])



