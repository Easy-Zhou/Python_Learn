#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-12 15:03:35.907396
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: os 模块的学习

import os

print(os.getcwd())  # 返回python解释器所在的目录,即调用python这个命令所在的目录
print(os.listdir())  # 查看传入目录的文件,若不传入则默认为当前路径
# os.remove("path")  # 用来移除一个文件
# os.removedirs("path")  用来移除一个目录