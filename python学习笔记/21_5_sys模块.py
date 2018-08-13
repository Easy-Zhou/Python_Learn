#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-13 12:21:50
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: sys模块的学习

import sys

print(sys.argv[0])  # 命令行参数列表,第一个元素是程序本身路径,之后的元素是程序输入的参数
print(sys.argv)
#sys.exit(0)  # sys.exit(n)  退出程序, 正常退出为0 或者其他信息 ,如'bye'
print(sys.version)  # 获取Python解释程序的版本信息
print(sys.maxsize)
# Python 3.0没有sys.maxint，因为Python 3的int是任意长度的
# 但是，sys.maxsize可以用作大于任何实际列表或字符串索引的整数。它符合实现的“自然”整数大小，并且通常
# 与同一平台上以前版本中的sys.maxint相同（假设具有相同的构建选项）。
print(sys.path)  # 返回模块的搜索路径,初始化时使用PYTHONPATH环境变量的值
print(sys.platform)  # 返回操作系统平台名称
sys.stdout.write("please:\n")  # 标准输出, 如引出进入条
# val = sys.stdin.readline()[:-1]  # 标准输入
print(sys.getrecursionlimit())  # 获取最大递归层数
sys.setrecursionlimit(1200)  # 设置最大递归层数
print(sys.getrecursionlimit())  # 获取最大递归层数
print(sys.getdefaultencoding())  # 获取解释器默认编码
print(sys.getfilesystemencoding())  # 获取内存数据存到文件里的默认编码