#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : CoderZ
# @File    : 
# @Software: PyCharm
# @Description:

# import test1
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)
from package_test import test1
test1.test()

