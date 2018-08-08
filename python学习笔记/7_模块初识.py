#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.03.31
# @Author  : CoderZ
# @File    :
# @Software: PyCharm
# @Description:
import sys

"""
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃       ┃
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

print(sys.path)  # path打印环境变量
# print(sys.argv)  # argv用来打印相对路径,在Pycharm中显示为绝对路径是因为Pycharm本身使用的就是绝对路径
# print(sys.argv[2])  # 在cmd中使用可以用来提取输入的参数 [0] 为文件本身的path(相对)

# import os
#
# cmd_res = os.system("dir")  # 一调用即执行,不保存结果
# cmd_res2 = os.popen("dir").read()  # os.popen命令是将执行的结果存在一个内存当中,需要用read()方法去调用信息,否则会输出内存地址
# print("--->", cmd_res)  # 输出0表示os.system()执行的命令成功
# print("--->", cmd_res2)
# os.mkdir("new_dir")  # 用来创建文件夹


# a, b, c = 1, 3, 5  # 分别给a,b,c赋值
# d = a if a > b else c  # 三元运算 result = 值(1) if 条件 else 值 (2)  如果条件为真: result = 值(1) 否则为 值(2)
# e = a if a < b else c
# print(d, e)
#
# msg = "我"
# print(msg)
# print(msg.encode(encoding="utf-8"))  # 在encode()中应填上之前是什么编码,在py3中默认参数为utf-8
# print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))  # 在decode()中要填想转成的是什么编码,在py3中默认参数为utf-8

# 打印进度条

import time

for i in range(50):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.5)

print()

time_format = "%Y-%m-%d %X"
time_current = time.strftime(time_format)
print(time_current)
