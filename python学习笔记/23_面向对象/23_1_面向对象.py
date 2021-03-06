#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/18 9:51
# @Author  : Zhou
# @File    : 23_1_面向对象.py
# @IDE     : PyCharm
# @Description: 23_1_面向对象


class Cal:

    def __init__(self, first_num, second_num):
        self.__first_num = first_num  # 属性名前加两个下划线是私有属性 但是外部可以通过A._A__N是可以访问到的，
        # 即这种操作并不是严格意义上的限制外部访问，仅仅只是一种语法意义上的变形
        self.__second_num = second_num
        print("构造函数")

    def __del__(self):
        print("析构函数")

    def __fun(self):
        print(self.__first_num, self.__second_num, "这是私有方法")

    def add(self):
        self.__fun()
        return self.__first_num + self.__second_num

    def multiply(self):
        return self.__first_num * self.__second_num

    def minus(self):
        return self.__first_num - self.__second_num

    def divide(self):
        return self.__first_num / self.__second_num


cal = Cal(5, 6)
print(cal.add())


class People():  # py2.7中父类要在括号内指定object

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "这是一个people类对象的实例"+self.name  # 用来在print的时候显示此内容，而不是默认的一串内存地址

    def self_introduce(self):
        print("my name is %s I'm %d years old" % (self.name, self.age))

    def eat(self):
        print("%s is eating" % self.name)

    def sleep(self):
        print("%s is sleeping" % self.name)


obj = People("zhou",18)
print("打印类的对象")
print(obj)


class Man(People):  # 这是继承了People类,这是单继承,多继承用逗号分隔开多个继承的类

    n = 100

    def __init__(self,name,age,sex):
        # People.__init__(self,name,age)  # 调用父类构造函数
        # super(Man,self).__init__(name,age)  # py2.7 的写法
        super().__init__(name,age)  # py3 的写法
        self.sex = sex
        self.__money = 10000000000

    def sleep(self):  # 重载父类方法
        # People.sleep(self)  # 调用父类方法
        print("-----------------------")
        super(Man, self).sleep()  # 调用父类方法
        super().sleep() # 调用父类方法
        print("A man is sleep")

    @staticmethod  # 静态方法
    def born():

        print("a child born",)

    @classmethod  # 类方法
    def population(cls):
        print("The population of man is ",cls.n)  # 调用了一个类变量

    @property  # 属性方法
    def test_property(self):
        """属性方法,把一个方法变成一个静态属性,调用不需要加括号
        将一个类的函数定义成特性以后，对象再去使用的时候obj.name,
        根本无法察觉自己的name是执行了一个函数然后计算出来的，
        这种特性的使用方式遵循了统一访问的原则,
        python并没有在语法上把它们三个内建到自己的class机制中，在C++里一般会将所有的所有的数据都设置为私有的，
        然后提供set和get方法（接口）去设置和获取，在python中通过property方法可以实现
        """
        return "eet"
    @property  # 相当于设置getter
    def money(self):
        return self.__money

    @money.setter # 设置setter
    def money(self,money):
        self.__money = money

m1 = Man("Bob", 22, "Male")
m1.sleep()


print(Man.test_property)  # 调用property方法
print(Man.test_property.__doc__)
m1.money = 10.2 # set
print(m1.money) # get


# get and set 方法例子

class get_set_test:
    """

    """
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name


te = get_set_test("tt",12)

print(te.name)
te.name = "ps"
print(te.name)

'''
像g1.life_value之类的属性引用，会先从实例中找life_value然后去类中找，
然后再去父类中找...直到最顶级的父类。那么如何解释下面的打印结果呢？
class Foo:
    def f1(self):
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')
        self.f1()

class Bar(Foo):
    def f1(self):
        print('Bar.f1')


b=Bar()
b.f2()

# 打印结果:
# Foo.f2
# Bar.f1
'''

'''
类中定义的__x只能在内部使用，如self.__x，引用的就是变形的结果。
这种变形其实正是针对外部的变形，在外部是无法通过__x这个名字访问到的。
在子类定义的__x不会覆盖在父类定义的__x，因为子类中变形成了：_子类名__x,而父类中变形成了：
_父类名__x，即双下滑线开头的属性在继承给子类时，子类是无法覆盖的。
这种变形需要注意的问题是：
1、这种机制也并没有真正意义上限制我们从外部直接访问属性，知道了类名和属性名就可以拼出名字：
_类名__属性，然后就可以访问了，如a._A__N
2、变形的过程只在类的定义是发生一次,在定义后的赋值操作，不会变形
'''

