#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/01
# @Author  : CoderZ
# @File    : list.py
# @Software: PyCharm
# @Description: 学习列表
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

import copy

names = ["第0个元素", "第1个元素", "第2个元素", "第3个元素", "第2个元素", "第2个元素"]
names.append("第4个元素")  # append 用来追加
names.insert(1, "第n个元素")  # insert的两个参数分别是(插入位置,插入的值)

names[5] = "新的元素"  # 改names中的值,但是不能越界
print(names)
# delete
names.remove("新的元素")  # 删除
del names[1]
names.pop(0)  # 括号中不填参数则默认删除最后一个值
print(names)
print(names.index("第1个元素"))  # 查找元素的下标
print(names[names.index("第1个元素")])
print(names.count("第2个元素"))
names.reverse()  # 反转:将数组反过来
print("reverse", names)
names.sort()  # 排序
print("sort", names)
names2 = ["names2中的元素0", "names2中的元素2"]
names.extend(names2)  # 合并
print("extend", names, names2)
del names2  # 删除变量
names.clear()  # 清空
print("clear", names )

myList = ["one", "two", "three", ["four_one", "four_two"], "five"]
myList2 = myList.copy()  # 属于浅copy
# myList2 = myList[:]   也是一种浅copy方式
# myList2 = list(myList)也是一种浅copy
print(myList, myList2)
myList2 = copy.copy(myList)  # 需要用copy模块 和上述的浅copy类似
print("copy.copy", myList, myList2)
myList2 = copy.deepcopy(myList)
myList[1] = "two_changed"
myList[3][0] = "four_one_changed"
print("deepcopy", myList, myList2)  # 深copy

cart = []
cart.append(['iphoneX', 10000])
cart.append(['iphoneX', 10000])
print(cart)
# print(names[0], names[2])
# print(names[1:3])  # 切片:表示取出从限定的起始位置到末尾之前的一个(左闭右开)
# print(names[-1])  # 切片
# print(names[-2])
# print(names[-3:-1])  # 切片只能从做往右,不能反过来,写[-1:3]是错的
# print(names[-3:])  # 要取最后面的值在后面不用加限定 -1 也可以省略
# print(names[0:3])
# print(names[:3])  # 切片时0也可以省略
# print(names[0:-1:2]  # 挑着切片

L1 = [i * 2 for i in range(10)]  # 列表生成式
print(L1)