# coding=utf-8
# @Time     :2020/4/13 0013 0:11
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func07.py
# @Software :PyCharm

# 装饰器
'''
加入购物车，付款，修改收货地址.....
判断用户的登陆状态

'''


def func(number):
    a = 100

    def inner_func():
        nonlocal a
        nonlocal number
        number += 1
        for i in range(number):
            a += 1

        print('修改后的a:', a)

    return inner_func


# 调用func
f = func(5)
f()


# 函数作为参数
a = 50
f1 = func(a)  # a 是一个实参
print(f1)

# 地址引用
def test():
    print('---------test----------')


t = test
print(t)