#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 14:26
# @Author  : Zhou
# @File    : 21_13_re模块正则.py
# @IDE     : PyCharm
# @Description: 21_13_re模块正则

import re

s = 'abc123d'
# re.match 从头开始搜索,匹配则返回一个对象,需要用group才能取出值
match_res = re.match('[0-9]',s)
if match_res:
    print(match_res.group())
# re.search 进行全局搜索,搜索到第一个匹配项即返回,需要用group才能取出值
search_res = re.search('[0-9]',s)
if search_res:
    print(search_res.group())
# re.findall 进行全局搜索,并把搜索到的所有内容到保存到一个列表中
findall_res = re.findall('[0-9]',s)
print(findall_res)