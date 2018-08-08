#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZY
import getpass
# getpass不能在Pycharm中直接运行,需要在cmd中运行
username = input("username:")
password = getpass.getpass("password:")

print(username, password)
