#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZY

username = input("username:")
password = input("password:")
if username == "zhouyi" and password == "zhouyi":
    print("Welcome!")
elif username == "zhouyi" and password != "zhouyi":
    print("Sorry,your password is wrong!")
else:
    print("Sorry,username does not exist!")
