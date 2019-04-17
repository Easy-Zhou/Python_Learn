#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.07.31
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: 函数的学习


def test(x):  # 定义函数
    """这是文档描述,需要三重双引号"""
    x += 1
    return x


print(test(3))


def func1():
    """此处定义了一个过程,相当于没有返回值的函数"""
    print("Hello!")


func1()


def func2():
    """函数可以返回多个值,以一个元组的形式将返回的多个值打包返回"""
    return 1, 'hello', ['test', 'test2'], {"name": "zhou"}


print(func2())
a, b, c, d = func2()
print(a, b, c, d)


def func3(x, y):
    """参数的形式,可通过关键字调用,不需要一一对应"""
    print(x, y)


func3(1, 3)
func3(y=2, x=2)
func3(3, y=2)


# func3(x=2, 3) 关键字不能在位置参数前面


def func4(x, y=2):
    """默认参数,默认参数位置上可以不进行赋值"""
    print("x=", x, "y=", y)


func4(2, 4)
func4(2)


# 参数组一定要在形参的最后一个

def func5(*args):
    """参数组的使用,将多个值存入一个元组"""
    print(args)


func5(1, 2, 3, 4)
func5(*[1, 2, 3, 4, 5])  # 想当于agrs = tuple([1, 2, 3, 4, 5]


def func6(x, *args):
    print("x = ", x, "args =", args)


func6(2, 3, 5, 6, 7)


def func7(**kwargs):
    """字典的参数组,把关键字参数转换成字典的方式"""
    print(kwargs)


func7(name="zhou", age=18, sex="Male")
func7(**{"name": "zhou", "age": 18})  # 相当于 kwargs = {"name": "zhou", "age": 18}  # 参数传递时的序列解包，若是非字典则用的是一个*


def demo(a, b, c):
    print(a + b + c)


seq = [1, 2, 3]
demo(*seq)  # 非字典的序列解包
dic = {1: 'a', 2: 'b', 3: 'c'}
demo(*dic)  # 6
demo(*dic.keys())  # 6
demo(*dic.values())  # abc
dic2 = {'a': 1, 'b': 2, 'c': 3}
demo(*dic2)  # abc
demo(**dic2)  # 相当于demo(a=1,b=2,c=3)


def func8(name, sex="M", **kwargs):
    print(name, kwargs, sex)


func8("zhou", age=18, sex="F")  # 默认参数不能添加到字典中去


def func9(name, age=18, *args, **kwargs):  # args 只能接收位置参数
    print(name, age, args, kwargs)


func9("zhou", 23, 23, "F", sex="M")

# 全局变量不能在函数的中进行修改除非申明global,不建议这么更改

name = "zhou"


def change_name():
    """全局变量不能在函数的中进行修改除非申明global,不建议这么更改"""
    global name
    global sex
    name = "yu"
    sex = "Female"


change_name()
print("changed_name = ", name, sex)  # 也可以在函数中定义全局变量,不建议这么使用


# 列表字典集合中的内容可以在函数中修改

# 高阶函数,把函数本身传给另一个函数作为参数
# 返回值中包含函数名(可以不修改函数的调用方式)


def add(a, b, f):
    return f(a) + f(b)


res = add(3, -6, abs)
print(res)


def bar():
    print("In the bar")


def func(f):
    print("decorate bar")
    f()
    print("decorate bar")
    return f


bar = func(bar)
bar()  # 这样就不会修改函数的调用方式了


# 嵌套函数

def foo():
    print("in the foo")

    def bar1():
        print("in the bar")

    bar1()


foo()
import math


def calculateCircle(r):
    if isinstance(r, (int, float)):
        print(r ** 2 * math.pi)
    else:
        print('input integer or float num')
