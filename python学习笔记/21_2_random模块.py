#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.08.10
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: random模块的学习

import random
print(random.random())  # 用于生成一个0到1随机浮点数: 0<= n < 1.0

print(random.randint(1, 7))  # 用于生成一个指定范围内的整数  a <= n <= b

print (random.randrange(1,10)) #5
#random.randrange的函数原型为：random.randrange([start], stop[, step])，
# 从指定范围内，按指定基数递增的集合中 获取一个随机数。如：random.randrange(10, 100, 2)，
# 结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。
# random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效。
print(random.choice('liukuni')) #i
#random.choice从序列中获取一个随机元素。
# 其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。
# 这里要说明一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。
# list, tuple, 字符串都属于sequence。有关sequence可以查看python手册数据模型这一章。
# 下面是使用choice的一些例子：
print(random.choice("学习Python"))#学
print(random.choice(["JGood","is","a","handsome","boy"]))  #List
print(random.choice(("Tuple","List","Dict")))   #List
print(random.sample([1,2,3,4,5],3))    #[1, 2, 5]
#random.sample的函数原型为：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。

print(random.uniform(1, 2))  # 指定一个区间返回浮点数

print(random.shuffle([1,2,3,4,5,6]))  # 洗牌的功能,打乱顺序

#############################################验证码demo##################################################

confirm_code = ""

seed_1 = [i for i in range(65,91)]
seed_2 = [i for i in range(97,123)]

seed_1.extend(seed_2)
seed_all = seed_1
# print(seed_all)

for i in range (5):
    temp = random.randint(0,4)
    if temp == i:
        tmp = chr(random.choice(seed_all))
    else:
        tmp = str(random.randint(0,9))
    confirm_code += tmp

print(confirm_code)

