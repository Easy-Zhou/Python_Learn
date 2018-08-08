#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/01 22:24
# @Author  : CoderZ
# @File    : ShoppingCart
# @Software: PyCharm
# @Description: 一个控制台的购物车程序,通过控制台输入来进行交互
"""
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓            ┃      ☃      ┃
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
salary = input('请输入您的工资:')
if salary.isdigit():  # 判断是否是数字
    salary = int(salary)
else:
    print("输入的不是数字")
pre_salary = salary
commodity = (("iphoneX", 9699), ("Mac Pro", 12000), ("TADA68 Pro", 600), ("raspberry pie", 360))
cart = []
while True:
    for i in range(len(commodity)):
        print(i+1, commodity[i][0], "¥" + str(commodity[i][1]))
    command = input(">>>:")
    if command == 'q':
        print("你购买了以下的商品:")
        for i in range(len(cart)):
            print(i + 1, cart[i][0], "¥" + str(cart[i][1]))
        print("总计:", "¥" + str(pre_salary - salary))
        print("余额:", "¥" + str(salary))
        break
    elif commodity[int(command)-1][1] > salary:
        print("穷逼,你买不起了")
    else:  # commodity[int(command)][1] < salary:
        print(commodity[int(command)-1][0]+"已加入购物车")
        salary -= commodity[int(command)-1][1]
        cart.append([commodity[int(command)-1][0], commodity[int(command)-1][1]])





