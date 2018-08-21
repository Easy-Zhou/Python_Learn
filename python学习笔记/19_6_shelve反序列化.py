#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-13 23:37:10
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: shelve反序列化

import shelve

f = shelve.open('OtherFile/shelve_test')  # 打开一个文件

print(f['name'])
print(f['info_dic'])

# del d['test']  # 进行删除
# f['test'] = [1,2,3,4]  # 添加
# f['name'] = names = ['joy','box','kid',2]  # 修改,只能整个进行修改
print(f['test'])
f.close()