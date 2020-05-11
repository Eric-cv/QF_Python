# coding=utf-8
# @Time     :2020/4/15 0015 23:15
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :text.py
# @Software :PyCharm

a = 100


def func(b):
    a = 10

    def inner_func():
        # a = 1
        print(a, b)

    # inner_func()
    return inner_func  # 返出内层函数


# 调用外部函数
f = func()
f()  # 外面调用内层函数

def zhuang(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('-----')
    return wrapper
@zhuang
def f1():
    pass

f1()
