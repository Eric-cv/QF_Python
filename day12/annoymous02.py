# coding=utf-8
# @Time     :2020/4/16 0016 0:14
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :annoymous02.py
# @Software :PyCharm

# map :对列表(或其他可迭代的如元组)里的元素进行操作时经常用，比如都+1，*2此类的

list1 = [3, 4, 6, 7, 8, 9, 9, 0, 2, 5]

result = map(lambda x: x + 2, list1)
print(list(result))  # [5, 6, 8, 9, 10, 11, 11, 2, 4, 7]

# for index, i in enumerate(list1):
#   list1[index] = i +2

func = lambda x: x if x % 2 == 0 else x + 1
result = func(5)
print(result)
# 对列表中的奇数进行+1操作
result = map(lambda x: x if x % 2 == 0 else x + 1, list1)
print(list(result))

# for index, i in enumerate(list1):
#   if i % 2!=0:
#       list1[index] = i +2
# print(list1)


# reduce()  对列表（或可迭代的）中的元素进行加减乘除运算的函数
from functools import reduce

tuple1 = (3, 5, 7, 8, 9, 1)
result = reduce(lambda x, y: x + y, tuple1)
print(result)

tuple2 = (1,)
# def reduce(function, sequence, initial=None):
#    pass
result = reduce(lambda x, y: x + y, tuple2, 10)
print(result)

# 动手测试减法，乘法

# filter
list1 = [12, 6, 8, 98, 34, 36, 2, 8, 0]
result = filter(lambda x: x > 10, list1)
print(result)
print(list(result))


def func(list1):
    list2 = []
    for i in list1:
        if i > 10:
            list2.append(i)
    return list2

# sorted
students = [
    {'name': 'tom', 'age': 20},
    {'name': 'lucy', 'age': 19},
    {'name': 'lily', 'age': 13},
    {'name': 'mark', 'age': 21},
    {'name': 'jack', 'age': 23},
    {'name': 'steven', 'age': 18},
]

# 找出所有年龄大于20岁的学生
result = filter(lambda x: x['age'] > 20, students)
print(list(result))

# 按照年龄大小排序
students = sorted(students, key=lambda x: x['age'])
print(students)

students = sorted(students, key=lambda x: x['age'], reverse=True)
print(students)

'''
max()
min()
sorted()

map()
reduce()
filter()
'''