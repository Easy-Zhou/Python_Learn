#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.04.14
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: 字符串方法举例练习
"""
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

"""
步骤:
1.---
2.---
3.---
"""

name = "test"
print(name.capitalize(), " # 首字母大写")
print(name.count("t"), " # 计算字符串中某字符的数量")
print(name.center(50, "*"), " # 将字符串居中显示,并用其他字符补全")
print(name.endswith("x"), " # 判断是否以某字符结尾,并返回True or False")
print(name.startswith('t'), " # 判断是否以某字符开始,并返回True or False")
tab = "start \tend"
print(tab.expandtabs(tabsize=10), " # 来改变tab符号转变成空格的长度")
print(name.find("e"), name.find("i"), " # 找到某字符在字符串中的位置,0开头 如果未找到则返回-1")
name2 = "my name is dadada"
print(name2[name2.find("name"):], " # 用途为字符串的切片，字符串也可切片")
exmp = "my name is {name} and my age is {age}"
print(exmp.format(name="dadada", age=18), " # 用于格式化输出")
print(exmp.format_map({"name": "dadada", "age": 18}), " # 用于格式化输出,采用字典的方法")
print("abc12".isalnum(), "# 判断是否包含数字和英文字符")
print("4334".isdigit(), " # 判断是否只由数字组成,不包括小数")
print("12".isdecimal(), "#判断是否为十进制数")
print("233".isnumeric(), " # 判断是否只由数字组成,不包括小数, 只针对unicode对象")
print("dg".isidentifier(), " #isidentifier 判断是否是一个合法的变量名")
print("tetA".islower(), " #islower 判断是否小写")
print("My Name Is".istitle(), " #istitle 判断是否为标题,标题的每个单词首字符大写")
print("My Name Is".isprintable(), " #isprintable 判断是否是可打印的,只要用于linux中的tty文件")
print("dgt".isupper(), " #isupper 判断是否是大写")
print("".join(['1', '2', '3']), " # join 的用法")
print(",".join(['1', '2', '3']), " # join 的用法")
print("ljust用法".ljust(20, "$"), " #ljust 类似去center的用法不够的用后面的字符在左边补全")
print("rjust用法".rjust(20, "$"), " #rjust 类似去center的用法不够的用后面的字符在右边补全")
print("ttt".upper(), " #upper 转大写")
print("TTT".lower(), " #lower 转小写")
print("\nstrip去掉两边的换行\n".strip(), " #strip 去除左右的空格和回车")
print("\nstrip去掉两边的换行\n".lstrip(), " #lstrip 去除左边的空格和回车")
print("\nstrip去掉两边的换行\n".rstrip(), " #rstrip 去除右边的空格和回车")
p = str.maketrans("abcdef", '123456')
print("adtdht".translate(p), " #translate 使用maketrans来进行转换")
print("end")
print("tt".replace("t", "a", 1), " #replace  将t替换成a后的数字为替换几个")
print("examle.a".rfind('a'), "#rfind 从右往左开始找，找到以一个a，a 在字符串中的第几位")
print('m la lk le ls lt lr lans'.split(' l'), "#split 按某字符或字符串分隔，并以列表的形式存储")
print('m la lk le\nls lt lr lans'.splitlines(), "#splitlines 按换行分隔，并以列表的形式存储")
print('exMAple'.swapcase(), "#swapcase 进项字符串大小写互换")
print('this is title'.title(), "#title 转换成Title")
print('xs'.zfill(20), "不足的用0填充在前")
