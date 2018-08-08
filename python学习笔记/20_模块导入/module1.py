#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.08.05
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: 模块与包的导入

import os,sys

# print(__file__)  # __file__ 返回的是一个相对路径
# print(os.path.abspath(__file__))  # 返回了绝对路径
# print(os.path.dirname(os.path.abspath(__file__)))  # 返回此文件的目录名

ABSPATH = os.path.abspath(__file__)
MODULE = os.path.dirname(ABSPATH)
PY = os.path.dirname(MODULE)
LEARN = os.path.dirname(PY)
# print(ABSPATH, MODULE, PY, LEARN)

for i in sys.path:
    print(i)

import python学习笔记

python学习笔记.O_Test.test()