#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-13 23:37:10
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: shelve序列化

import shelve

f = shelve.open('OtherFile/shelve_test')  # 打开一个文件,会自动生成三个文件 分别是.bak .dat .dir

names = ['joy','box','kid']
info = {'name':'joy','age': '18'}

f['name'] = names  #  持久化列表
f['info_dic'] = info

f.close()