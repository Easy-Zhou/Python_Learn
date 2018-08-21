#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 9:40
# @Author  : Zhou
# @File    : 24_异常处理.py
# @IDE     : PyCharm
# @Description: 24_异常处理


list_1 = [1, 2, 3, 4]
dict_1 = {"name": "zhou", "age": 18}

filename = "OtherFile/sss"
try:
    # print(list_1[4])
    # print(dict_1['sex'])
    with open(filename,'r') as f:
        f.read()

except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

except (KeyError,IndexError) as e:  # 可以将两个错误写在一起
    print("wrong", e)
# except IndexError as e:
#     print("out of bounds", e)
except Exception as e:  # 抓取所有错误
    print("wrong", e)

else:
    print("只有没有错误才会执行")

finally:
    print("不管有没有错都会执行")
