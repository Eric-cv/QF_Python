# coding=utf-8
# @Time     :2020/4/12 0012 0:34
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func03.py
# @Software :PyCharm


# 闭包
# 在函数中提出的概念，
'''
条件：
1.外部函数中定义了内部函数
2.外部函数是有返回值的
3.返回的值是：内部函数名
4.内部函数还引用了外部函数的变量

格式：
def 外部函数():
    ...
    def 内部函数():
        ...
    return 内部函数


'''
def func():
    a = 100

    def inner_func():
        b = 99
        print(a, b)

    # print(locals())
    return inner_func


# x 就是你的内部函数，函数名+括号就表示调用函数
x = func()  # <function func.<locals>.inner_func at 0x000001EB92EC2730>
x()
