#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.08.03
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: 迭代器学习 有next方法

from collections import Iterable  # 可迭代的 (相当于可以作用于for循环 list tuple set dict generator
from collections import Iterator  # 迭代器

print(isinstance([1,2],Iterable))
print(dir([2,3]),"打印可调用的方法")  # 有next方法的就是迭代器

print(isinstance((x for x in range(10)),Iterator))
print(isinstance([1,2],Iterator))

# 通过iter方法就可以将可迭代方法变成一个迭代器
print(isinstance(iter([1,2]),Iterator))

# python2.7 中xrange是一个迭代器 Python3中range直接就是迭代器
