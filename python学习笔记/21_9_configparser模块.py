#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-16 10:09:19
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: configparser模块 用于解析配置文件 读取之后每个项下的数据以字典的形式保存
# [DEFAULT]为默认项,内部的变量是全局的变量,之后在读每个其他节点的时候都会有DEFAULT节点中的变量,
# 但是其他节点中重新声明了DEFAULT中的某个变量则可以被覆盖


import configparser

conf = configparser.ConfigParser()

conf.read("OtherFile/conf_1.ini")

print(conf.sections())
print(conf.default_section)

print(list(conf['bitbucket.org'].keys()))
print(conf['topsecret.server.com']['Forward'])

for k,v in conf['topsecret.server.com'].items():
    print(k,v)

conf2 = configparser.ConfigParser()

conf2.read("OtherFile/conf_2.ini")
print(dir(conf2))

print(conf2.options('group1'))   # 取到group1的值
print(conf2['group1']['k2'])

conf2.add_section('group3')
conf2['group3']['name'] = 'test'

conf2.write(open('OtherFile/conf_2.ini','w'))
# 因为conf中包含了整个配置文件的内容,因此写回的时候需要用w模式来覆盖,不能用a模式来追加

conf2.remove_option('group1','k1')
conf2.write(open("OtherFile/conf_3.ini",'w'))

conf2.remove_section('group3')
conf2.write(open("OtherFile/conf_4.ini",'w'))