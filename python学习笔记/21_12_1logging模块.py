#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 22:17
# @Author  : Zhou
# @File    : 21_12_logging模块.py
# @IDE     : PyCharm
# @Description: logging--日志管理
# 日志级别 : debug >>> info >>> warning >>> error >>> critical
'''
对应的等级
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
'''

import logging
import sys

# 直接输出
# logging.warning("this is a warning!")
# logging.critical("OMG this is a critical error")

'''写入文件'''
logging.basicConfig(filename='OtherFile/log_test.log',
                    filemode='a',  # 文件打开方式,默认为'a'还可以是'w'
                    level=logging.DEBUG,  # level表示只写入与此level相同级别或更高的信息
                    format='%(asctime)s ##%(levelno)s %(levelname)s## %(message)s',
                    datefmt='%Y-%m-%d %I:%M:%S %p')
                    # stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件，
                    # 默认为sys.stderr。若列出了filename则不能列出stream

logging.debug("this is a debug log")
logging.info("this is a info log")
logging.warning("this is a warning log")
logging.error("this is a error log")
logging.critical("this is a error log")

'''
format参数中可能用到的格式化串：
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息
'''
