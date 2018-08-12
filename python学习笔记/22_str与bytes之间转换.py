#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-12 15:08:53.496487
# @Author  : CoderZ
# @File    :
# @Software: PyCharm
# @Description: str与bytes之间转换

# bytes object
b = b"example"

# str object
s = "example"

# str to bytes
bytes(s, encoding="utf8")

# bytes to str
str(b, encoding="utf-8")

# an alternative method
# str to bytes
str.encode(s)

# bytes to str
bytes.decode(b)