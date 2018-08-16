#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-16 09:05:08
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: XML模块

from xml.etree import ElementTree as ET

#####################################第一种创建方式#####################################
# 创建根节点
root = ET.Element("famliy")


# 创建节点大儿子
son1 = ET.Element('son', {'name': '儿1'})
# 创建小儿子
son2 = ET.Element('son', {"name": '儿2'})

# 在大儿子中创建两个孙子
grandson1 = ET.Element('grandson', {'name': '儿11'})
grandson2 = ET.Element('grandson', {'name': '儿12'})
son1.append(grandson1)
son1.append(grandson2)


# 把儿子添加到根节点中
root.append(son1)
root.append(son1)

tree = ET.ElementTree(root)
tree.write('OtherFile/output1.xml',encoding='utf-8', short_empty_elements=False)
#####################################第一种创建方式#####################################


#####################################第二种创建方式#####################################
# 创建根节点
root = ET.Element("famliy")


# 创建大儿子
# son1 = ET.Element('son', {'name': '儿1'})
son1 = root.makeelement('son', {'name': '儿1'})
# 创建小儿子
# son2 = ET.Element('son', {"name": '儿2'})
son2 = root.makeelement('son', {"name": '儿2'})

# 在大儿子中创建两个孙子
# grandson1 = ET.Element('grandson', {'name': '儿11'})
grandson1 = son1.makeelement('grandson', {'name': '儿11'})
# grandson2 = ET.Element('grandson', {'name': '儿12'})
grandson2 = son2.makeelement('grandson', {'name': '儿12'})

son1.append(grandson1)
son1.append(grandson2)


# 把儿子添加到根节点中
root.append(son1)
root.append(son2)

tree = ET.ElementTree(root)
tree.write('OtherFile/output2.xml',encoding='utf-8', short_empty_elements=False)
#####################################第二种创建方式#####################################


#####################################第三种创建方式#####################################
# 创建根节点
root = ET.Element("famliy")


# 创建节点大儿子
son1 = ET.SubElement(root, "son", attrib={'name': '儿1'})
# 创建小儿子
son2 = ET.SubElement(root, "son", attrib={"name": "儿2"})

# 在大儿子中创建一个孙子
grandson1 = ET.SubElement(son1, "age", attrib={'name': '儿11'})
grandson1.text = '孙子'


et = ET.ElementTree(root)  #生成文档对象
et.write("OtherFile/output3.xml", encoding="utf-8", xml_declaration=True, short_empty_elements=False)
#####################################第三种创建方式#####################################


#####################################第四种创建方式#####################################
from xml.dom import minidom


def prettify(elem):
    """将节点转换成字符串，并添加缩进。
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

# 创建根节点
root = ET.Element("famliy")


# 创建大儿子
# son1 = ET.Element('son', {'name': '儿1'})
son1 = root.makeelement('son', {'name': '儿1'})
# 创建小儿子
# son2 = ET.Element('son', {"name": '儿2'})
son2 = root.makeelement('son', {"name": '儿2'})

# 在大儿子中创建两个孙子
# grandson1 = ET.Element('grandson', {'name': '儿11'})
grandson1 = son1.makeelement('grandson', {'name': '儿11'})
# grandson2 = ET.Element('grandson', {'name': '儿12'})
grandson2 = son2.makeelement('grandson', {'name': '儿12'})

son1.append(grandson1)
son2.append(grandson2)


# 把儿子添加到根节点中
root.append(son1)
root.append(son1)


raw_str = prettify(root)

f = open("OtherFile/output4.xml",'w',encoding='utf-8')
f.write(raw_str)
f.close()
#####################################第四种创建方式#####################################