#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.07.31
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: 学习字符编码

# 需要通过Unicode进行中转

s = "你好"

s_gbk = s.encode("gbk")
print("gbk:", s_gbk)

print("utf-8:", s.encode())  # encode 不填写参数默认按P有charm的编码utf8来编码

gbk_to_utf8 = s_gbk.decode("gbk").encode("utf-8")
print(gbk_to_utf8)

