#!/usr/bin/env python3
# -*- coding: utf-8 -*-

names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# 避免key不存在的错误
print('Thomas' in d, d.get('Thomas'), d.get('Thomas', -1))

# delete key
d.pop('Bob')

# 和list比较，dict有以下几个特点：
# 1. 查找和插入的速度极快，不会随着key的增加而变慢；
# 2. 需要占用大量的内存，内存浪费多。

# dict的key必须是不可变对象

# set
s = set([1, 2, 3])
s.add(4)
s.remove(4)
