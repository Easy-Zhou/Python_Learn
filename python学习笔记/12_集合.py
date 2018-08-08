#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.07.29
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: 集合的学习

# 作用：去重，关系测试
# 特性：无序

list_1 = [1,4,5,6,5,4,3]
list_1 = set(list_1)


print(list_1, type(list_1))

list_2 = {2,4,5,6,7,65} # set literal 效率比调用set函数更高
print(list_1, list_2)

a = frozenset({1, 2, 3, 4, 5})  # 不可变集合,不能够改变集合内部的元素
print(a)

# 交集
print("\n\n")
print(list_1.intersection(list_2),"#intersection 交集")
print(list_1 & list_2, "& 交集")

# 并集
print("\n\n")
print(list_1.union(list_2), "#union 并集")
print(list_1 | list_2, "| 并集")

# 差集
print("\n\n")
print(list_1.difference(list_2),"#difference 差集")
print(list_1 - list_2, "- 差集")

# 子集
print("\n\n")
print(list_1.issubset({1,3,4,5,6,7}),"#issubset 是否为后一项的子集")

# 超集/父集
print("\n\n")
print(list_1.issuperset({1,3,4,5}),"#issuperset 是否为后一项的超集")

# 对称差集/对称差分 并集减交集
print(list_1.symmetric_difference(list_2),"#symmetric_difference 对称差分 并集减交集")
print(list_1 ^ list_2, "#^ 对称差分 并集减交集")

# 如果交集为空返回True
print({1,2,3}.isdisjoint({4,5}),"#isdisjoint 如果交集为空返回True")

# 添加 add 和 update方法
print("\n\n添加add 和 update方法")
list_1.add(123)
print(list_1)
list_1.update({23,34,56})
print(list_1)

# 删除 remove
print("\n\n删除 remove")
list_1.remove(123) # 如果不存在会报错
print(list_1)
# list_1.remove({23,34,56}) 会删除整个集合
# print(list_1)
list_1.pop()
print(list_1,"# pop随机删一个")

list_1.discard(3) # 不存在也不会报错




# 判断是否在一个集合里
print(23 in list_1,"# in")

