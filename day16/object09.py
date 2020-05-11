# coding=utf-8
# @Time     :2020/4/30 0030 12:19
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :object09.py
# @Software :PyCharm


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print('------>eat1')
#
#     def eat(self, food):  # 第二个eat方法会把第一个eat方法覆盖
#         print('------>eat:', food)
#
# p =Person('jack')
# p.eat()  # TypeError: eat() missing 1 required positional argument: 'food'
# p.eat('狮子头')


# 多继承
class Base:
    def test(self):
        print('----Base----')


class A(Base):
    def test(self):
        print('---->AAAA')


class B(Base):
    def test(self):
        print('---->BBBB')


class C(Base):
    def test(self):
        print('---->CCCC')


class D(A, B, C):
    pass


d = D()
d.test()
# import inspect
# print(inspect.getmro(D))
print(D.__mro__)  # 查看多继承的搜索顺序

'''
python允许多继承，
def 子类(父类1, 父类2,...):
    pass    
如果父类中有相同的
'''
