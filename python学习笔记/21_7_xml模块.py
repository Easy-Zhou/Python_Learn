#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-15 18:54:52
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: XML模块

from xml.etree import ElementTree as ET

############ 解析方式一 ############
"""
# 打开文件，读取XML内容
str_xml = open('OtherFile/xml_test.xml', 'r').read()

# 将字符串解析成xml特殊对象，root代指xml文件的根节点
root = ET.XML(str_xml)
"""
############ 解析方式二 ############

# 直接解析xml文件
tree = ET.parse("OtherFile/xml_test.xml")

# 获取xml文件的根节点
root = tree.getroot()

# 顶层标签

print(root.tag)

# 遍历XML文档的第二层
for child in root:
    # 第二层节点的标签名称和标签属性 标签属性以字典的形式返回
    print(child.tag, child.attrib,"===", child.text, "==")

    # 遍历XML文档的第三层
    for i in child:
        # 第三层节点的标签名称和内容
        print(i.tag, i.attrib, i.text)


# 遍历XML中所有的year节点
for node in root.iter('year'):
    # 节点的标签名称和内容
    print(node.tag, node.text)

# 循环所有的year节点
for node in root.iter('year'):
    # 将year节点中的内容自增一
    new_year = int(node.text) + 1
    node.text = str(new_year)

    # 设置属性
    node.set('name', 'alex')
    node.set('age', '18')
    # 删除属性
    del node.attrib['name']

###########删除节点############
# 遍历data下的所有country节点
for country in root.findall('country'):
    # 获取每一个country节点下rank节点的内容
    rank = int(country.find('rank').text)

    if rank > 50:
        # 删除指定country节点
        root.remove(country)


############ 保存文件 ############
tree = ET.ElementTree(root)
tree.write("OtherFile/newnew.xml", encoding='utf-8')

