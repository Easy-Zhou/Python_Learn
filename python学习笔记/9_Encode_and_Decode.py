#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.07.27
# @Author  : CoderZ
# @File    :
# @Software: PyCharm
# @Description: Encode和Decode使用

info = '''encode 使用语法
str.encode(encoding='UTF-8',errors='strict')
encoding -- 要使用的编码，如: UTF-8。
errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace',
'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
'''

Str = "encode使用"
str_utf8 = Str.encode("UTF-8")
str_gbk = Str.encode("GBK")

print(Str)
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)

print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
print("GBK 解码：", str_gbk.decode('GBK', 'strict'))


info2 = '''
bytes.decode(encoding="utf-8", errors="strict")
encoding -- 要使用的编码，如"UTF-8"。
errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace',
'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
'''
