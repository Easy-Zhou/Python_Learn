#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.07.29
# @Author  : CoderZ
# @File    : OtherFile/*
# @Software: PyCharm
# @Description: 文件操作

import time
Time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

data = open("OtherFile/gbkfile.txt").read()
# 因为Windows默认的字符编码为GBK(ANSI使用多个字节来代表一个字符的各种汉字延伸编码方式的总称在简体中文Windows操作系统中，
# ANSI 编码代表 GBK 编码
print(data)
data = open("OtherFile/yesterday",encoding="utf-8").read() # 若文件编码格式为utf-8 需要设置encoding 使用utf-8编码格式打开
print(data)

# 正常操作

f = open("OtherFile/yesterday",encoding="utf-8")

data = f.read()
print(data)
print("line".center(30, '-'))
data2 = f.read()  # 此时没有读到任何内容,因为文件的指针以及到达文件末尾
print(data2)
f.close()

f = open("OtherFile/write_model",'w',encoding="utf-8")  # w是写模式,open时就是创建一个新文件
f.write(" w是写模式,open时就是创建一个新文件")

f = open("OtherFile/append_model",'a',encoding="utf-8")  # a是append模式追加,可写(追加)但是不能读
f.write("文件进行一次读写\n")
# print(f.read())
f.close()

f = open("OtherFile/append_model","r",encoding="utf-8") # r是只读模式

count = 0
for line in f:
    if count == 9:
        print("line".center(30,'-'))
        count += 1
        continue
    print(line.rstrip())
    count +=1

# 读取1000位的圆周率
with open("OtherFile/pi_million_digits.txt",'r',encoding="utf-8") as file_object:  # 建议使用with的方式来打开文件,会自动帮你关闭文件
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()
print(pi_string[: 20])

# "+" 表示可以同时读写某个文件
# r+，可读写文件。【可读；可写；可追加】 r+如果之前没有read则在文件开头添加,会覆盖之前的内容(写的长度),如果read或者更改光标的位置
# 则总光标位置处开始写,也会覆盖之前的内容
# w+，写读
# a+，同a
# with open("OtherFile/+_model.txt","r+",encoding="utf-8") as file_object:
#     # file_object.write("\nThe Time is:" + Time)
#     data = file_object.read()
#
# print(data)


# "U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）
#
# rU
# r+U



# "b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）
#
# rb
# wb
# ab
with open("OtherFile/binary","wb") as f:
    f.write("Hello binary\n".encode())  #将字符串转换成二进制格式写入. 写入之后的文件则是以二进制编码,但是显示的依然是字符串


# file的一些方法
with open("OtherFile/yesterday","r",encoding="utf-8") as f:
    print(f.tell(),"#tell 根据字符的个数来读取当前指针所在位置")
    print(f.readline(5))
    print(f.tell())

    f.seek(0) # 回到某个地方,0 是最开始的位置

    print(f.encoding,"#encoding 是打印文件的编码")
    print(f.fileno(),"#fileno 返回此文件句柄的接口编号")
    print(f.seekable(),"#seekable 判断文件是否可以调回光标")

    print(f.flush(),"#flush 强制将写入到缓存中的内容写入硬盘中,无返回")
    print(f.closed, "#closed 判断文件是否关闭,返回TRUE Or False")

# with open("OtherFile/yesterday", "a", encoding="utf-8") as f:
#     f.truncate(20)  # 从文件开头开始截取20个字符 不能是读的模式


# 对文件修改
print("# 对文件修改")

with open("OtherFile/yesterday","r",encoding="utf-8") as f1, \
        open("OtherFile/yesterday.bak","w",encoding="utf-8") as f2:
    for line in f1:
        if "舌尖上的雨露" in line:
            line = line.replace("舌尖","额头")
        f2.write(line)

