#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.07.28
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: 实现一个三级菜单，打印省市县，可返回上一级，可随时退出

menu = {
    "Zhejiang": {
        "Hangzhou": {
            "Jiande": {},
            "Fuyang": {},
            "Tonglu": {}
        },
        "Wenzhou": {
            "Ouhaiqu": {},
            "Luchengqu": {},
            "Longwanqu": {}
        },
        "Taizhou": {},
        "Ningbo": {}
    },
    "Shanghai": {
        "Pudong": {
            "Lujiazui": {}
        },
        "Xuhui": {
            "2": {}
        }
    }
}

exit_flag = False
current_layer = menu
layers = [menu]

while not exit_flag:
    for i in current_layer:
        print(i)
    temp = input("input>>>").strip()
    if temp == "q":
        exit_flag = True
        break
    elif temp == "b":
        if len(layers) > 1:
            layers.pop()
            current_layer = layers[-1]
        else:
            print("这是我的极限了!!!")
    elif temp not in current_layer:
        continue
    else:
        if len(current_layer[temp]) < 1:
            print("我是有底线的！！！")
        else:
            current_layer = current_layer[temp]
            layers.append(current_layer)

