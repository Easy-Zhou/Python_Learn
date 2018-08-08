#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZY

username = 'testuser'
password = 'testpasswd'
count = 3
flag = 0
while count > 0:
    In_username = input('usrname:')
    In_password = input('password:')
    count -= 1
    fp = open('user.txt', 'r')
    judge = fp.readline()
    fp.close()
    if In_username == username and judge == 'block':
        print('this usrname is blocked.')
    elif In_username == username and In_password == password:
        print('Welcome login')
    elif In_username == username and flag == 2:
        file = open('user.txt', 'w+')
        file.writelines('block')
        file.close()
        print('sorry you have input wrong password for three times,this usrname is blocked.')
    elif In_username == username and In_password != password:
        flag += 1
        # print(flag)
        print('sorry you input a wrong password,please try again')
    else:
        print('sorry this username is not exist')
else:
    print('sorry you wrong three times, please try after 30min')



