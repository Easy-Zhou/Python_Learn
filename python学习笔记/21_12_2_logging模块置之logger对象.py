#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 11:56
# @Author  : Zhou
# @File    : 21_12_2_logging模块置之logger对象.py
# @IDE     : PyCharm
# @Description: 21_12_2_logging模块置之logger对象

import logging
from logging import handlers

# 定义filter的一个类,类的名字随意

class IgnoreZhouFilter(logging.Filter):
    """忽略Zhou的日志"""
    def filter(self, record): # 固定写法
        return "Zhou" not in record.getMessage()

# 生成logger对象
logger = logging.getLogger('test1')
logger.setLevel(logging.DEBUG)  # 默认的日志级别是warning

# 把filler对象添加到logger中
logger.addFilter(IgnoreZhouFilter())

# 生成handler对象
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)  # handle 设置的日志级别如果比logger对象的高则可以覆盖,否则不能覆盖
fh = logging.FileHandler('OtherFile/test_1.log')
fh1 = handlers.RotatingFileHandler(filename="OtherFile/test_size.log",
                                   maxBytes=10, # 设置单个文件的最大值
                                   backupCount=3)  # 设置保留的文件个数
fh2 = handlers.TimedRotatingFileHandler(filename="OtherFile/test_time.log",
                                        when="S", # 时间间隔的单位 S秒 M 分 H小时 D天 W 每星期(interval=0 时代表星期一) midnight每天凌晨
                                        interval=5, # 时间间隔大小
                                        backupCount=3)
sh.setLevel(logging.WARNING)

# 将handler对象绑定到logger
logger.addHandler(sh)
logger.addHandler(fh)
logger.addHandler(fh1)
logger.addHandler(fh2)

# 生成formatter对象
stream_formatter = logging.Formatter('%(asctime)s -%(name)s- ##%(levelno)s %(levelname)s## %(message)s')
file_formatter = logging.Formatter('%(asctime)s -%(name)s- ##%(levelno)s %(levelname)s line:%(lineno)d ## %(message)s'
                                      ,datefmt='%Y-%m-%d %I:%M:%S %p')

# 把formatter对象绑定到handler对象
sh.setFormatter(stream_formatter)
fh.setFormatter(file_formatter)
fh1.setFormatter(file_formatter)
fh2.setFormatter(file_formatter)

# 输出日志

logger.debug("this is a debug log")
logger.info("this is a info log")
logger.warning("this is a warning log Zhou")
logger.error("this is a error log")
logger.critical( "this is a error log")