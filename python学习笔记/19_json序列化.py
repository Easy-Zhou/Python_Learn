#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.08.04
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: json and pickle 序列化

import json

info = {
    "name": "周易",
    "age": 18
}

with open("OtherFile/temp.json","w") as f:
    f.write(json.dumps(info))  # json 序列化(变成字符串)

# with open("OtherFile/temp.json","r") as f:
#     data = json.loads(f.read())  # json 反序列化(将字符串转换成相应的数据)

# print(data['age'])





