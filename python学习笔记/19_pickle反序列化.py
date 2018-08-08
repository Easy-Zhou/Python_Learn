#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.08.04
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: pickle反序列化

import pickle

def say(name):
    print("this is another function\nhello,", name)


with open("OtherFile/temp.pkl","rb") as f:
    #data = pickle.loads(f.read())
    data2 = pickle.load(f)  # 上下两个方法相同

#data['func']("zho")
data2['func']("zho")
