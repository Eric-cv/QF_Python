# coding=utf-8
# @Time     :2020/4/25 0025 17:53
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :object02.py
# @Software :PyCharm

# 函数 和类里面定义的：方法
# def func(name):
#     print('---->', name)
#
#
# username = 'admin'
# func(username)
#
#
# def func(names):
#     for name in names:
#         print(name)
#
#
# name_list = ['aa', 'bb', 'cc']
# func(name_list)


class Phone:
    # 魔术方法之一,魔术方法格式： __名字__()
    def __init__(self):  # init初始的，初始化
        # 动态的给self空间中添加属性（self空间就是传进来的对象的地址，即对象空间）
        self.brand = 'xiaomi'
        self.price = 4999

    def call(self):  # self是不断发生改变的，谁调用self就是谁，self传的是不同的对象
        print('---->call')
        print('价格：', self.price)  # 不能保证每个self里面都存在price


p = Phone()  # 一个内存地址
p.call()  # p.call() p调用call，python底层就把p的地址作为参数传给self
p1 = Phone()   # 另一个内存地址
p1.price = 5999  # 更改p1的price
p1.call()
# print(Phone.price)  # type object 'Phone' has no attribute 'price'
