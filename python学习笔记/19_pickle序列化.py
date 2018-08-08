#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :  2018.08.04
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: pickle序列化 pickle 只支持python但是其支持Python的所有数据类型,包括函数等,但json只支持简单的数据

import pickle


def say(name):
    print("hello,", name)

info = {
    "name": "zhu",
    "age": 18,
    "func": say
}

with open("OtherFile/temp.pkl","wb") as f:
    # f.write(pickle.dumps(info))
    pickle.dump(info, f)  # 等同于上面的方法

