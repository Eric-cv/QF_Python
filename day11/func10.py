# coding=utf-8
# @Time     :2020/4/15 0015 21:11
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func10.py
# @Software :PyCharm

'''
如果装饰器是多层的，谁离函数最近就优先使用哪个装饰器
'''
# 装饰器
def zhuang1(func):
    print('------->1 start')

    def wrapper(*arg, **kwarg):
        func()
        print('刷漆')

    print('-------> 1 end')
    return wrapper

def zhuang2(func):
    print('------->2 start')

    def wrapper(*arg, **kwarg):
        func()
        print('装门')

    print('-------> 2 end')
    return wrapper

@zhuang2
@zhuang1
def house():
    print('我是毛坯房.....')

house()