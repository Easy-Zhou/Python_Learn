#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018.08.03
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: 内置方法

abs(-2)
print(all([0, 3, -2]), "#all 中全部为真则返回True")
print(any([0, 2]), "#any 中有一个为真则返回True, 内容为空也为False")

t = ascii([2, 3, "t"])
print(t, type(t), "#ascii 把内存的变量变成一个可打印的字符串的形式")
print(eval(t), "#eval 把字符传转换成有效的表达式")
print(type(bin(7)), bin(7), "#bin 十进制转二进制的字符串形式")

# bool的使用与any类似
print(bool([1, 0, 2]), "#bool ")
print(bool([]))

a = bytes("abcd", encoding="utf-8")
b = bytearray("abcde", encoding="utf-8")  # 变成可变的bytes字符串
print(b[1], "# ascii字符")

print(callable(callable), "# 判断是否可调用(其后可加括号)")

print(chr(97), "#chr 返回ASCI码对应的字符")
print(ord('A'), "#ord 返回字符对应的ASCII码")

code = '''
for i in range(0, 10, 2):
    print(i)
'''
py_obj = compile(code, "err.log", "exec")  # 底层编译
print(py_obj, type(py_obj))
exec(py_obj)
exec(code)

print(complex(2 + 4j), "# 复数")

dict()  # 生成一个字典
dir({})  # 返回可调用方法
print(divmod(5, 2), "#divmod 相除并返回商和余数")

a = "{1: 'a', 2: 'b'}"
b = eval(a)
print(b, type(b), "#eval 将字符串str当成有效的表达式来求值并返回计算结果。结合math当成一个计算器非常好用")

(lambda n: print(n))(5)
cal = lambda n: n if n < 4 else n - 4
print(cal(5))

res = filter(lambda n: n > 5, range(10))  # 返回一个迭代器
for i in res:
    print(i)

res = map(lambda n: n * n, range(10))  # 将后面的值让前边的参数进行处理
print(type(res))
for i in res:
    print(i)

from functools import reduce

res = reduce(lambda x, y: x * y, range(1, 5))
# 对前面一个参数f的结果进行累加或累乘 比如x为range的第一个数或者上一步计算的结果,y为range接下来的一个数值
print(res)

a = frozenset({1, 2, 3, 4, 5})  # 不可变集合,不能够改变集合内部的元素
print(a)



hash("zhou")  # 生成该对象的哈希数值

a = hex(152)
b = oct(152)
print(a, type(a))  # 将数字转成16进制的字符串, bin是二进制,Oct是八进制
print(b, type(b))  # 将数字转成8进制的字符串

print(globals())  # 返回整个本身文件的key-values的列表

def test():
    local_var = 123
    print(locals())  # 因为globals无法获取到函数内部的局部变量,只能通过locals获取,与globals类似


test()

__builtins__.print("tett","builtins 内置模块的名字空间")
a = pow(2, 4)  # 2**4
print(a)
a = pow(2, 4, 3)  # pow(2,4) % 3  2**4%3
print(a)

t = 2 + 3
b = repr(t)  # 将表达的或者列表等转换成字符串
print(eval(b))

x = round(1.23)
print(x)
x = round(1.2345, 2)
print(x)

my_slice = slice(1, 5, 2)  # slice(start, stop ,step) slice(stop),slice(start,stop) 设置一个切片的方式
x = [1.2, 3, 4, 5, 6, 7]
print(x[my_slice])

a = {6: 2, 8: 0, 1: 4, 5: 10, -6: 12}
print(sorted(a.items()))  # 按key来排序
print(sorted(a))
print(sorted(a.items(), key=lambda x:x[1]))  # 按value来排序

a = [1,2,3,4]
b = ['a', 'b', 'c', 'd']

for i in zip(a,b):  # zip 还是迭代器
    print(i)


__import__("0_Test")  # 等同于 improt 0_Test
