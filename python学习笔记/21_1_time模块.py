#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.08.10
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: time 模块的学习

import time

# print(time.clock()) #返回处理器时间,3.3开始已废弃 , 改成了time.process_time()测量处理器运算时间,不包括sleep时间,不稳定,mac上测不出来
print(time.altzone)  #返回与utc时间的时间差,以秒计算\
print(time.asctime()) #返回时间格式"Fri Aug 19 11:14:16 2016",
print(time.localtime()) #返回本地时间 的struct time对象格式
print(time.gmtime(time.time()-800000)) #返回utc时间的struc时间对象格式

print(time.asctime(time.localtime())) #返回时间格式"Fri Aug 19 11:14:16 2016",
print(time.ctime()) #返回Fri Aug 19 12:38:29 2016 格式, 同上


# 日期字符串 转成  时间戳
string_2_struct = time.strptime("2016/05/22","%Y/%m/%d") #将 日期字符串 转成 struct时间对象格式
print(string_2_struct)
# #
struct_2_stamp = time.mktime(string_2_struct) #将struct时间对象转成时间戳
print(struct_2_stamp)


# 将时间戳转为字符串格式
print(time.gmtime(time.time()-86640)) #将utc时间戳转换成struct_time格式
print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()) ) #将utc struct_time格式转成指定的字符串格式

# 时间加减
import datetime

print(datetime.datetime.now()) #返回 2018-08-10 22:13:18.238426
print(datetime.date.fromtimestamp(time.time()) )  # 时间戳直接转成日期格式 2018-08-10
print(datetime.datetime.now() )
print(datetime.datetime.now() + datetime.timedelta(3)) #当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分


#
c_time  = datetime.datetime.now()
print(c_time.replace(minute=3,hour=2)) #时间替换

'''
%a    本地（locale）简化星期名称    
%A    本地完整星期名称    
%b    本地简化月份名称    
%B    本地完整月份名称    
%c    本地相应的日期和时间表示    
%d    一个月中的第几天（01 - 31）    
%H    一天中的第几个小时（24小时制，00 - 23）    
%I    第几个小时（12小时制，01 - 12）    
%j    一年中的第几天（001 - 366）    
%m    月份（01 - 12）    
%M    分钟数（00 - 59）    
%p    本地am或者pm的相应符    一    
%S    秒（01 - 61）    二    
%U    一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。    三    
%w    一个星期中的第几天（0 - 6，0是星期天）    三    
%W    和%U基本相同，不同的是%W以星期一为一个星期的开始。    
%x    本地相应日期    
%X    本地相应时间    
%y    去掉世纪的年份（00 - 99）    
%Y    完整的年份    
%Z    时区的名字（如果不存在为空字符）    
%%    ‘%’字符
'''