#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.08.04
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: json反序列化

import json

with open("OtherFile/temp.json", "r") as f:
    data = json.loads(f.read())  # json 反序列化(将字符串转换成相应的数据)

print(data['age'])