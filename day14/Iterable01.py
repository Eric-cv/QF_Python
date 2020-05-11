# coding=utf-8
# @Time     :2020/4/25 0025 14:26
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :Iterable01.py
# @Software :PyCharm

# 可迭代的对象：1.生成器 2.元组 列表 集合 字典 字符串
# 如何判断一个对象是否是可迭代的?
from collections import Iterable

list = [1, 4, 7, 8, 8]
print(isinstance(list, Iterable))  # True
print(isinstance('abc', Iterable))  # True
print(isinstance(100, Iterable))  # False

g = (x + 1 for x in range(10))
print(isinstance(g, Iterable))  # True

'''
迭代是访问集合元素的一种方式。迭代器是一个可以记住遍历的位置的对象。
# 特点：
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
迭代器只能往前不会后退。
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

可迭代的 是不是肯定就是 迭代器？
生成器是可迭代的，也是迭代器
list是可迭代的，但不是迭代器
list ---> iter(list) ---> 迭代器 next()
'''
list1 = [1, 2, 3, 4, 5]
print(next(list1))  # >>> 'list' object is not an iterator


list1 = iter(list1)  # 通过iter函数将可迭代的变成迭代器
print(next(list1))  # 1
print(next(list1))  # 2

'''
生成器与迭代器关系：

'''