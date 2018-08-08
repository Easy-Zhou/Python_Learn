#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: 测试

import time

Time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

with open("OtherFile/test.txt","r+") as f:
    # f.readline()
    f.seek(50)
    f.write(Time + "\n")
    f.flush()
with open("OtherFile/test.txt","r+") as f:
    data = f.read()

print("data" + data)

def test():
    print("in the test")