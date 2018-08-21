#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/20 18:36
# @Author  : Zhou
# @File    : 23_2_metaclass.py
# @IDE     : PyCharm
# @Description: 23_2_metaclass

class Foo():

    def __init__(self, name):
        self.name = name


f = Foo("zhou")

print(type(f))
print(type(Foo))


###########定义一个类的新方法############ 创建类的本质
def func(self):
    print("My name is %s and I'm %d years-old" % (self.name, self.age))


def __init__(self, name, age):
    self.name = name
    self.age = age


Foo2 = type('Foo', (), {'func1': func,
                        '__init__': __init__})
###########定义一个类的新方法############
f2 = Foo2("zhou", 18)
f2.func1()
print(type(Foo2))

# python 2
# class MyType(type):
#     def __init__(self,*args,**kwargs):
#
#         print("Mytype __init__",*args,**kwargs)
#
#     def __call__(self, *args, **kwargs):
#         print("Mytype __call__", *args, **kwargs)
#         obj = self.__new__(self)
#         print("obj ",obj,*args, **kwargs)
#         print(self)
#         self.__init__(obj,*args, **kwargs)
#         return obj
#
#     def __new__(cls, *args, **kwargs):
#         print("Mytype __new__",*args,**kwargs)
#         return type.__new__(cls, *args, **kwargs)
#
# print('here...')
# class Foo(object,metaclass=MyType):
#
#
#     def __init__(self,name):
#         self.name = name
#
#         print("Foo __init__")
#
#     def __new__(cls, *args, **kwargs):  # 触发__init__ 将实例化
#         print("Foo __new__",cls, *args, **kwargs)
#         return object.__new__(cls)
#
# f = Foo("Alex")
# print("f",f)
# print("fname",f.name)

# 自定义元类