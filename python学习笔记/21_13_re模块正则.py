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
match_res = re.match('[0-9]', s)
if match_res:
    print(match_res.group())
# re.search 进行全局搜索,搜索到第一个匹配项即返回,需要用group才能取出值
search_res = re.search('[0-9]', s)
if search_res:
    print(search_res.group())
# re.findall 进行全局搜索,并把搜索到的所有内容到保存到一个列表中
findall_res = re.findall('[0-9]', s)
print(findall_res)

# re.split 按规则进行分割re.split(pattern,string,maxsplit=0,flags=0) maxsplit 设置的是分割几个匹配项
s = "sdtse12setre33seee23dd|gg-ee"
res = re.split('\d+|\W+', s)
print(res)

# re.sub 替换
res = re.sub("\d+",
             '_', s,
             count=2) # count表示替换几个匹配项
print(res,"re.sub")

# re.fullmatch(pattern,string,flags=0) 整个字符串匹配成功就返回re 对象,否则返回None
res = re.fullmatch('\w+@\w+\.(com|cn|edu)',"mailtojoy@gmail.com")
print(res,"fullmatch")

# re.compile()
pattern = re.compile('\w+@\w+\.(com|cn|edu)')
res = pattern.fullmatch("mailtojoy@gmail.com")  # 同上一步的操作,但是compile会提前把表达式编译好后保存,
# 若进行大量匹配时可以节省时间
print(res)

# Flags标志符
'''
re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
M(MULTILINE): 多行模式，改变'^'和'$'的行为
S(DOTALL): 改变'.'的行为,make the '.'special character match any character at all, 
including a newline; without this flag, '.' will match anything except a newline.
X(re.VERBOSE) 可以给你的表达式写注释，使其更可读，下面这2个意思一样
'''
print(re.search('foo.$','foo1\nfoo2\n',re.MULTILINE).group() ,"会匹配到foo1")


'''匹配规则'''
# . 默认匹配\n之外的任意一个字符
s = '12sfhhf343kf1k1213klsd'
res = re.search('.', s)
print(res)

# ^ 匹配以^后的字符开头
res = re.search('^2', s)  # 等效于match
print(res)

# $ 匹配以$之前字符结尾
res = re.search('3$', s)
print(res)

# * 匹配*号之前的字符0-n个
res = re.search('[a-z0-9]*', s)
print(res)

# + 匹配+号之前的字符1-n个
res = re.search('[0-9]+', s)
print(res)

# ? 匹配之前的字符0-1次
res = re.search('[0-9]?', s)
print(res)
'''
当?紧随任何其他限定符(*,+,?,{n},{n.},{n,m})之后时匹配模式是非贪婪模式
“贪婪模式”总是尝试匹配尽可能多的字符；“非贪婪模式”则相反，
总是匹配尽可能少的字符。例如，用"ab*"如果用于查找"abbbc"，
将找到"abbb"。而如果使用非贪婪的数量词"ab*?"，将找到"a"。
'''

# {m} 匹配之前的字符m个
res = re.search('[0-9]{2}', s)
print(res)

# {m,n} 匹配之前字符的m至n个{,n}0-n {n,}n-max
res = re.findall('[a-z]{,3}', s)
print(res)

# | 匹配 | 左或右的字符 总是先对左边进行匹配一旦成功则跳过右部的
res = re.search('[a|b]test', 'atest')
print(res)

# (...) 分组匹配,将匹配到的结果分开
res = re.search('([a-z]+)([0-9]+)', 'test123')
print(res.groups())

'''
\A 只从开头匹配,相当于^
\Z 匹配字符结尾,相当于$
\d 匹配数字0-9
\D 匹配非数字
\w 匹配[a-zA-Z0-9]
\W 匹配非[a-zA-Z0-9]
\s  匹配空白字符 \t \n \r
'''

# (?P<name>...)分组匹配
tmp = "(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})"
tem_s = "330182200007182658"
res = re.search(tmp, tem_s)
print(res.groups())
print(res.groupdict())
