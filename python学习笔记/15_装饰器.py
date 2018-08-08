#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.08.01
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: 装饰器学习 (又名语法糖)

# 原则: 对于被装饰的函数来说是透明的
# 不能修改本装饰的函数的源代码
# 不能修改函数调用的方式
# 高阶函数 + 嵌套函数

import time


def Timer(func):
    """这是一个用于计算函数运行时间的装饰器"""

    def deco():
        star_time = time.time()
        func()
        stop_time = time.time()
        print("The function running time is:%s" % (stop_time - star_time))

    return deco


@Timer  # 相当于操作 test1 = Timer(test1) 添加在需要被装饰的函数头部
def test1():
    time.sleep(2)
    print("This is function test1")


test1()


def Timer2(func):
    """这是一个用于计算函数运行时间的装饰器"""

    def deco(*args, **kwargs):
        star_time = time.time()
        res = func(*args, **kwargs)  # 接收原函数的返回值,并在函数最后返回
        stop_time = time.time()
        print("The function running time is:%s" % (stop_time - star_time))
        return res

    return deco


@Timer2
def test1():
    time.sleep(2)
    print("This is function test1")
    return "Test1 is over"


@Timer2
def test2(name, age):
    time.sleep(1)
    print("This is function test2")
    print("name is %s, age is %d" % (name, age))


print(test1())
test2("zhou", 18)

username1 = "yu"
password1 = "b"
username2 = "w"
password2 = "n"


def auth(type):
    def out(fun):

        def deco(*args, **kwargs):
            username = input("username:")
            password = input("password:")
            res = None
            if type == "one":
                if username == "yu" and password == "b":
                    res = fun(*args, **kwargs)
                else:
                    print("wrong, try again")
            elif type == "two":
                if username == "w" and password == "n":
                    res = fun(*args, **kwargs)
                else:
                    print("wrong, try again")
            return res

        return deco

    return out


@auth("one")
def function1():
    print("welcome to function1")
    return "this is function1"


@auth(type="two")
def function2(name):
    print(name, "welcome to function2")
    return "this is function2"


print(function1())
print(function2("Python"))

