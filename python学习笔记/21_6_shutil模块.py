#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-13 13:24:58
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: shutil 模块的学习

import shutil

with open('OtherFile/pi_million_digits.txt', 'r') as f1, \
        open('OtherFile/Dir1/pi_million_digits_bak.txt', 'w') as f2:
    shutil.copyfileobj(f1, f2)  # 将文件内容拷贝到另一个文件中

shutil.copyfile("OtherFile/temp.json","OtherFile/Dir1/temp_backup.json")  # 拷贝文件
shutil.copymode("OtherFile/temp.json","OtherFile/Dir1/temp_backup.json")  # 仅拷贝文件的权限. 内容,组,用户均不变
shutil.copystat("OtherFile/temp.json","OtherFile/Dir1/temp_backup.json")  # 拷贝状态信息,包括, mode bits, a_time,m_time,flags
shutil.copy("OtherFile/temp.json","OtherFile/Dir1/temp_backup.json")  # 拷贝文件和权限
shutil.copy2("OtherFile/temp.json","OtherFile/Dir1/temp_backup.json")  # 拷贝文件和状态信息
# shutil.ignore_patterns('*.jpg','*.txt')
shutil.copytree("OtherFile","newFile",ignore=shutil.ignore_patterns('*.txt'))  # 递归的去拷贝文件,ignore是排除的文件
#shutil.rmtree("newFile")  # 递归删除
#shutil.move('OtherFile/Dir1/.pytest_cache','.pytest_cache')  # 递归的去移动文件

# shutil.make_archive(base_name,format...)
# 创建压缩包并返回文件路径，例如：zip、tar
#
# base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
# 如：www                        =>保存至当前路径
# 如：/Users/wupeiqi/www =>保存至/Users/wupeiqi/
# format：	压缩包种类，“zip”, “tar”, “bztar”，“gztar”
# root_dir：	要压缩的文件夹路径（默认当前目录）
# owner：	用户，默认当前用户
# group：	组，默认当前组
# logger：	用于记录日志，通常是logging.Logger对象

# ret = shutil.make_archive("OtherFile/Dir1/test",'zip',root_dir='.pytest_cache')  # 返回压缩文件的路径 自动回加上.zip
# print(ret)

# shutil 对压缩包的处理是调用 ZipFile 和 TarFile 两个模块来进行的，详细：
# import zipfile
#
# # 压缩
# z = zipfile.ZipFile('laxi.zip', 'w')
# z.write('a.log')
# z.write('data.data')
# z.close()
#
# # 解压
# z = zipfile.ZipFile('laxi.zip', 'r')
# z.extractall()
# z.close()
#
# zipfile 压缩解压

# import tarfile
#
# # 压缩
# tar = tarfile.open('your.tar','w')
# tar.add('/Users/wupeiqi/PycharmProjects/bbs2.zip', arcname='bbs2.zip')
# tar.add('/Users/wupeiqi/PycharmProjects/cmdb.zip', arcname='cmdb.zip')
# tar.close()
#
# # 解压
# tar = tarfile.open('your.tar','r')
# tar.extractall()  # 可设置解压地址
# tar.close()
#
# tarfile 压缩解压