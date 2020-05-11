# coding=utf-8
# @Time     :2020/4/15 0015 21:22
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func11.py
# @Software :PyCharm

# 装饰器带参数
'''
带参数的装饰器是三层的
最外层的函数负责接收装饰器函数
里面的内容还是原装饰器的内容
'''


def outer(a):  # 第一层： 负责接收装饰器的参数
    def decorate(func):  # 第二层： 负责接收函数的
        def wrapper(*args, **kwargs):  # 第三层 ：负责接收函数的参数
            func(*args, **kwargs)
            print('------>铺地砖{}块..'.format(a))

        return wrapper  # 返出来的是：第三层
    return decorate    # 返回出来的是：第二层


@outer(a=10)
def house(time):
    print('我是{}日期拿到的房子的钥匙，我是毛坯房...'.format(time))

@outer(100)
def street():
    print('新修的街道名字是：黑泉路')



house('2019-6-12')
street()