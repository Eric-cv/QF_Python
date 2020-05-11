# coding=utf-8
# @Time     :2020/4/15 0015 20:02
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func09.py
# @Software :PyCharm

import time


# 登陆校验
def decorate(func):
    def wrapper(*args, **kwargs):# {‘clazz':'1904'}
        # **kwargs要求传入的必须是键值对的关键字参数，系统默认把关键字参数作为字典保存，放入kwarg中
        # **kwargs对传入的字典进行拆包，拆成关键字参数的形式
        # 即**kwargs拆包，kwargs打包
        print('正在校验中....')
        time.sleep(2)
        print('校验完毕....')
        # 调用原函数
        func(*args, **kwargs)  # f1 f2 f3

    return wrapper


@decorate
def f1(n):
    print('------f1------', n)


f1(5)  # 此时的f1是wrapper


@decorate
def f2(name, age):
    print('------f2 ------', name, age)


f2('lily', 20)


@decorate
def f3(students, clazz='1905'):  # 默认参数clazz = '1905'
    print('{}班级的学生如下'.format(clazz))
    for stu in students:
        print(stu)


students = ['lily', 'tom', 'lucy']
f3(students, clazz='1904')

@decorate
def f4():
    print('--------->f4')