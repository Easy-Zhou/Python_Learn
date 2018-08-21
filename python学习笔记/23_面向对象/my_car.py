#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/20 9:40
# @Author  : Zhou
# @File    : my_car.py
# @IDE     : PyCharm
# @Description: my_car 从car模块中导入Car/ElectricCar类

from car import Car, ElectricCar  # 或直接导入整个car模块

my_new_car = Car("audi",'a4',2016)
print(my_new_car.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())
