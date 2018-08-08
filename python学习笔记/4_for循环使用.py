#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/01
# @Author  : CoderZ
# @File    : for.py
# @Software: PyCharm
# @Description: for循环使用
"""
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

myList = ["one", "two", "three", "four", "five"]
commodity = (("iphoneX", 9699), ("Mac Pro", 12000), ("TADA68 Pro", 600), ("raspberry pie", 360))
print("1")
for i in myList:
    print(i)
else:
    print("wuxunhuan")
print("range")
for i in range(0, 10, 2):
    print(i)
print("range(len(myList))")
for i in range(len(myList)):
    print(i, myList[i])
print("range 二维")
for i in range(len(commodity)):
    print(i, commodity[i][0], commodity[i][1])
print("使用.index来查找下标")
for item in commodity:
    print(commodity.index(item), item)
print("使用enumerate的两种形式")
for index, item in enumerate(commodity):
    print(index, item)
for item in enumerate(commodity):
    print(item)
for i in range(1, 10):
    print(i)
# Python pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句，如下实例
