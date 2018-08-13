#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-12 15:03:35.907396
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: os 模块的学习

import os

print(os.getcwd())  # 返回python解释器所在的目录,即调用python这个命令所在的目录
print(os.listdir())  # 查看传入目录的文件,若不传入则默认为当前路径
# os.remove("path")  # 用来移除一个文件
# os.removedirs("path")  用来移除一个目录
os.getcwd() # 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  # 改变当前脚本工作目录；相当于shell下cd
os.curdir()  # 返回当前目录: ('.')
os.pardir()  #  获取当前目录的父目录字符串名：('..')
os.makedirs('dirname1/dirname2')   # 可生成多层递归目录
os.removedirs('dirname1')  #  若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')   # 生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')   # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')  #  列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.linesep() # 返货当前平台使用的终止符
os.remove("path")  # 删除一个文件
os.rename("oldname","newname")  # 重命名文件/目录
os.stat('path/filename')  # 获取文件/目录信息
os.sep()   # 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep()  #  输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep()   # 输出用于分割文件路径的字符串
os.name()   # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")  # 运行shell命令，直接显示
os.environ()  #获取系统所有的环境变量
os.getenv("APPDATA")  # 获取输入的指定环境变量的值
os.get_terminal_size()  # 获取终端大小
os.environ.setdefault("TEST","ttt")  # 设置系统环境变量
path = "path"
os.path.abspath(path) # 返回path规范化的绝对路径
os.path.split(path)  #将path分割成目录和文件名二元组返回
os.path.splitext(path)  # 分离扩展名
os.path.dirname(path)  #返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path) # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path) # 如果path存在，返回True；如果path不存在，返回False
os.path.getsize(path)  # 获取文件的大小
os.path.isabs(path) # 如果path是绝对路径，返回True
os.path.isfile(path) # 如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path) # 如果path是一个存在的目录，则返回True。否则返回False
#os.path.join(path1[, path2[, ...]]) # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.join('T1','T2','T3')  # 返回T1/T2/T3
os.path.getatime(path)  #返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)  #返回path所指向的文件或者目录的最后修改时间