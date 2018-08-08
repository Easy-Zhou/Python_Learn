#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.08.02
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: 生成器 generator 不访问 其中的数值不存在 可以节省开销(只保留一个值,只记住当前的位置) 只能通过循环进行访问
# 循环一次取完之后 因为已经到达最后的节点不能再继续往后,同时也不能往前,所以在循环啥也没有了

a = (i * 2 for i in range(10))
print(a)  # <generator object <genexpr> at 0x000002382C12DD00>  #
for i in a:
    if i == 10:
        break
    print(i)

print(a.__next__(), "调用下一个数据")
# print(a.__next__())
print(a)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 保存了函数的中断状态
        a, b = b, a + b
        n += 1
    return "done,这是生成器抛出的异常"


f = fib(100)
print("\n", f)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(next(f))

g = fib(10)

while True:
    try:
        x = next(g)
        print("g:", x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break

# 使用生成器来做并行计算 (协程)

import time


def consumer(name):
    print("%s 准备吃包子了" % name)
    while True:
        baozi = yield  # 到yield会停止
        print("包子{baozi}来了,被{name}吃了".format(baozi=baozi, name=name))


def producer(name):
    c = consumer("A")
    c2 = consumer("B")
    c.__next__()
    c2.__next__()
    print("开始准备做包子啦")
    for i in range(0, 10, 2):
        time.sleep(1)
        print("做了两个包子")
        c.send(i)  # send 唤醒yield 并被yield传一个值
        c2.send(i + 1)


producer("zho")
