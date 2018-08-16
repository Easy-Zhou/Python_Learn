#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-16 13:28:18
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: subprocess模块 用于调用系统命令

import subprocess


'''
subprocess.Popen(...)

用于执行复杂的系统命令

参数：
    args：shell命令，可以是字符串或者序列类型（如：list，元组）
    bufsize：指定缓冲。0 无缓冲,1 行缓冲,其他 缓冲区大小,负值 系统缓冲
    stdin, stdout, stderr：分别表示程序的标准输入、输出、错误句柄
    preexec_fn：只在Unix平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用
    close_sfs：在windows平台下，如果close_fds被设置为True，则新创建的子进程将不会继承父进程的输入、输出、错误管道。
    所以不能将close_fds设置为True同时重定向子进程的标准输入、输出与错误(stdin, stdout, stderr)。
    shell：同上
    cwd：用于设置子进程的当前目录
    env：用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承。
    universal_newlines：不同系统的换行符不同，True -> 同意使用 
    startupinfo与createionflags只在windows下有效
    将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如：主窗口的外观，进程的优先级等等 
'''


def sayhi():
    print("Hi")

'''run和Popen的主要区别是Popen会发起一个新的进程来执行结果,不会影响当前程序'''
a = subprocess.Popen('echo $PWD;sleep 2',shell=True,cwd='/tmp',stdout=subprocess.PIPE,preexec_fn=sayhi)
a.poll()  # 获取执行结果/状态
a.wait()  # 等待程序执行结束
a.terminate()  # 终止当前进程
a.kill()  # 强制停止当前进程  相当于os.kill(a.pid)
a.communicate(b'input content')  # 与发起的进程进行交互,只能交互一次
import signal
a.send_signal(signal=signal.SIGKILL)  # 发送信号

# 标准写法
# a = subprocess.run(['ping','-n','2','10.132.226.121'],stderr=subprocess.PIPE,stdout=subprocess.PIPE,check=True)
# check 是进行检查此命令是否有错误,默认为False
# stderr 是返回错误信息,一般有check=True 可以不用此选项
# stdout 是输出
a = subprocess.run(['ping', '-n', '2'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
print(str(a.stdout, encoding='gbk'))
print(a.args)
print(a.stderr)
print(a.returncode)

# 涉及到管道| 的命令要按如下的写
# subprocess.run('df -h | grep root', stderr=subprocess.PIPE, stdout=subprocess.PIPE, check=True,
#                shell=True)  # shell=True的意思是将这条命令直接交给系统去执行 不用run将命令拼起来

''' call,返回命令执行状态'''
ret = subprocess.call(['ping','localhost'])
print(ret)
ret = subprocess.call('ping localhost',shell=True)
print(ret)


'''check_call,执行命令，如果执行状态码是 0 ，则返回0，否则抛异常'''
# subprocess.check_call(["ls", "-l"])
# subprocess.check_call("exit 1", shell=True)

'''check_output,执行命令，如果状态码是 0 ，则返回执行结果，否则抛异常'''
# subprocess.check_output(["echo", "Hello World!"])
# subprocess.check_output("exit 1", shell=True)

