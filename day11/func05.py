# coding=utf-8
# @Time     :2020/4/12 0012 23:07
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func05.py
# @Software :PyCharm

# 闭包的应用
# 闭包
'''
1. 能够保存返回闭包时的状态(外层函数变量)

'''

'''
def func(a, b):
    c = 10

    def inner_func():
        s = a + b + c
        print('相加之后的结果是：', s)

    return inner_func


ifunc = func(6, 9)
ifunc1 = func(2, 8)
ifunc2 = func(1, 9)
# 当调用func(6, 9) ---> a=6, b=9 ---> inner_func()内部函数中--->返回内部函数
# （此时返回的内部函数已经记录此时的a和b的值，所以不会受到a,b改变影响）
# 再去调用func(2, 8) ---> a = 2, b = 8 --->保存在本次的inner_func函数中---》
#  返回的时候返回的就是保存2，8的内部函数

print(ifunc)
print(ifunc1)
print(ifunc2)

ifunc()  # 25
ifunc1()  # 20
ifunc2()  # 20
'''


# 计算器
def generate_count():
    container = [0]

    def add_one():
        container[0] = container[0] + 1  # [1]
        print('当前是第{}次访问'.format(container[0]))

    return add_one


# 内部函数就是一个计算器
counter = generate_count()
counter()  # 第1次访问
counter()  # 第2次访问
counter()  # 第3次访问
