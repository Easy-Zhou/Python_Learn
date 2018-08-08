#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :
# @Author  : CoderZ
# @File    :
# @Software: PyCharm
# @Description: 字典学习

info = '''
字典是一个key-value的数据类型（键值对）
字典的特性：
* dict是无序的
* key必须是唯一的，可能会用到去重操作
'''

info1 = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': 'XiaoZe Maliya',
}

# dict查找
print("\n\n查找")
print(info1)
print(info1['stu1101'], "# 字典查找")
# print(info1['stu1105'], "# 键不存在会报一个KeyError的错误")
print(info1.get('stu1104'), "# 键不存在则返回一个None，否则返回Value，建议使用此方法防止出错")
print(info1.get('stu1103'), "# 键不存在则返回一个None，否则返回Value，建议使用此方法防止出错")
# 判断某个键是否在dict里可以用in关键字
print('stu1102' in info1, "# 返回True Or False") # 在python2.x的版本中有info1.has_key("stu1102")

# dict元素的修改和添加
# 如果存在则修改value 不存在则重新创建一个键值对
print("\n\n修改")
info1['stu1101'] = "工藤新一"
print(info1, "# 修改")
info1['stu1104'] = "柯南"
print(info1, "# 添加")
new_dict = {
    "stu1101": "new_value",
    3: 4,
    2: 5
}
info1.update(new_dict)
print(info1, "#update 作用就是跟新已有的键值添加没有的键值对")

# 删除字典元素 del pop popitem三个方法
print("\n\ndict删除")
del info1['stu1101']
print(info1)
info1['stu1101'] = "再次添加"
print(info1)
info1.pop('stu1101')
print(info1)
info1.popitem()  # 随机删除因为dict是无序的
print(info1)

# 多级字典嵌套及操作
print("\n\n多级字典嵌套及操作")
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

av_catalog["大陆"]["1024"][1] += ",可以用爬虫爬下来"
print(av_catalog["大陆"]["1024"])
#ouput ['全部免费,真好,好人一生平安', '服务器在国外,慢,可以用爬虫爬下来']

# 其他的一些方法
print("\n\n其他的一些方法")
print(info1.values(), "#values 返回所有的value")
print(info1.keys(), "#keys 返回所有的key")
print(info1.setdefault("stu1103",{"www.baidu.com": [1, 2]}), "#setdefault 先去dict中搜索有没有此键，若有则返回原来的value"
                                                             "如果没有则新建一个key-value并返回新的value值")
print(info1)
print(info1.setdefault("stu1101",{"www.baidu.com": [1, 2]}), "#setdefault 先去dict中搜索有没有此键，若有则返回原来的value"
                                                             "如果没有则新建一个key-value并返回新的value值")
print(info1)
print(info1.items(), "#items 将dict转换成一个列表，每个键值对都是列表中的一组元组")

c = dict.fromkeys([1,2,3],"test")
print(c, "#fromkeys 用于初始化字典，但是有一个坑如下")

g = dict.fromkeys([1,2,3],[1,{"name": "old_name"},123])
print(g, "#fromkeys 原始状态")
g[2][1]["name"] = "Jack Chen"
print(g, "# 有多级的时候会把全部的都改了")
c[2] = "new"
print(c, "# 只有一级的时候不会有这个问题，和深浅拷贝以及内存地址有关")

# 字典的循环
print("\n\n字典的循环")
Dict = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': 'XiaoZe Maliya',
}

print("直接通过key取出value效率更高，建议使用")
for i in Dict:
    print(i, Dict[i])

print("使用item方法先将字典转换成列表，这样的效率相对于上一个循环来说更低，不建议使用")
for k,v in Dict.items():
    print(k, v)

