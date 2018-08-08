#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018.04.17-21:44
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description:
#
# 步骤:
# 1.---
# 2.---
# 3.---
#
#  code is far away from bugs with the god animal protecting
#     I love animals. They taste delicious.
#               ┏┓      ┏┓
#             ┏┛┻━━━┛┻┓
#             ┃      ☃      ┃
#             ┃  ┳┛  ┗┳  ┃
#             ┃      ┻      ┃
#             ┗━┓      ┏━┛
#                 ┃      ┗━━━┓
#                 ┃  神兽保佑    ┣┓
#                 ┃　永无BUG！   ┏┛
#                 ┗┓┓┏━┳┓┏┛
#                   ┃┫┫  ┃┫┫
#                   ┗┻┛  ┗┻┛


import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器,由生成器返回生成
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()

List = [1, 2, 3, 4]
it = iter(List)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
# for x in it:
#     print(x, end=" ")


