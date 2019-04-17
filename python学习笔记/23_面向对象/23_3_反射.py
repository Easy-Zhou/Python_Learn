#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/20 23:41
# @Author  : Zhou
# @File    : 23_3_反射.py
# @IDE     : PyCharm
# @Description: 23_3_反射

def bark(self):
    print("%s is yelling..." % self.name)


class Dog():

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating..." % self.name, food)


d = Dog("ppp")
choice = input(">>>:").strip()

if hasattr(d, choice):  # hasattr 判断类中是否含有此属性,或属性方法
    func = getattr(d, choice)  # getattr 获取属性方法的内存对象,或者属性的值
    func("zzz")
    # delattr(d.choice)  # 删除属性
else:
    setattr(d, choice, bark)  # 当设置属性方法时,第三个值为给赋给d.choice的方法名
    # 当设置属性时,第三个值为属性的值,choice则为属性的名称
    # 相当于 d.choice = bark
    d.bark1(d)
