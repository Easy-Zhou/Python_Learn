#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-12 15:08:53.496487
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: paramiko模块学习(用于ssh连接)

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.132.226.100', 22, 'root', 'root123')

stdin, stdout, stderr = ssh.exec_command('df -h')
a = stdout.read()

print(str(a, encoding='utf-8'))
ssh.close()
