# coding=utf-8
# @Time     :2020/4/9 0009 23:01
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func07.py
# @Software :PyCharm

# 函数的嵌套


def a():
    print('AAAAAA')


def b():
    # 调用函数a
    a()
    print('BBBBBB')


def c():
    b()
    print('CCCCCC')
# 调用b
# b()
# 调用c
c()