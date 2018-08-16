#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-08-16 10:40:19
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description: hashlib模块 用于加密

import hashlib

# ######## md5 ########
hash = hashlib.md5()
# help(hash.update)
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())
print(hash.digest())

######## sha1 ########

hash = hashlib.sha1()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())

# ######## sha256 ########

hash = hashlib.sha256()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())

# ######## sha384 ########

hash = hashlib.sha384()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())

# ######## sha512 ########

hash = hashlib.sha512()
hash.update(bytes('admin', encoding='utf-8'))
print(hash.hexdigest())

# ######## md5 ########
# 添加自定义的key进行进一步加密
hash = hashlib.md5(bytes('898oaFs09f', encoding="utf-8"))
hash.update(bytes('admin', encoding="utf-8"))
print(hash.hexdigest())

# python内置还有一个 hmac 模块，它内部对我们创建 key 和 内容 进行进一步的处理然后再加密
import hmac

h = hmac.new(bytes('898oaFs09f', encoding="utf-8"))
h.update(bytes('admin', encoding="utf-8"))
print(h.hexdigest())