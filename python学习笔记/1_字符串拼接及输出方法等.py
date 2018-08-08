#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/04/01 22:24
# @Author  : CoderZ
# @File    : print.py
# @Software: PyCharm
# @Description: 输出的一些方法,字符串格式化,拼接,有颜色的输出等
# name = input("name:")
# age = input("age:")
# job = input("job:")
# salary = input("salary")
name = "hh"
age = "20"
job = "IT"
salary = "60000"
print("字符串拼接法")
info = '''
---------info of '''+name+'''------
Name:'''+name+'''
Age:'''+age+'''
Job:'''+job+'''
Salary:'''+salary
print(info)

print("%s格式化输出")
age = int(age)  # 类型转换
info1 = '''
---------info of %s ------
Name: %s
Age: %d
Job: %s
Salary: %s
''' % (name, name, age, job, salary)
print(info1)

print("{}中填变量")
info2 = '''
---------info of {_name} ------
Name: {_name}
Age: {_age}
Job: {_job}
Salary: {_salary}
'''.format(_name=name, _age=age, _job=job, _salary=salary)
print(info2)

print("{}中填数字,类似C#")
info3 = '''
---------info of {0} ------
Name: {0}
Age: {1}
Job: {2}
Salary: {3}
'''.format(name, age, job, salary)
print(info3)

print('\033[5;31;2m这是一个有颜色的输出\033[0m')
pas = input("请输入用户密码，如果不设置，\033[5;33;40m请回车!\033[0m")
print("end")
