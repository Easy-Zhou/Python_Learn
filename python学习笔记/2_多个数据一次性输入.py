#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description:
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

"""
步骤:
1.---
2.---
3.---
"""

'''
t = int(input())
for i in range(t):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a + b > c:
        print("Case #%d: true" % (i + 1))
    else:
        print("Case #%d: false" % (i + 1))
# 连续输入整数方法:
str_in = input('用空格分隔多个数据:')
# 用空格分隔多个数据:123 456 789 111 222
num = [int(n) for n in str_in.split()]
print(num)
'''

a = int(input())
for i in range(a):
    b, c, d = map(int, input().split())
    # map(lambda x:int(x), input().split(' '))
    print("Case #" + str(i + 1) + ": true" if b + c > d else "Case #" + str(i + 1) + ": false")
