# coding=utf-8
# @Time     :2020/4/30 0030 17:00
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :calculate.py
# @Software :PyCharm

# __all__ = ['number', 'add', 'Calculate']
# 变量
number = 100
name = 'calculate'


def add(*args):
    if len(args) > 1:
        sum = 0
        for i in args:
            sum += i
        return sum
    else:
        print('至少传入两个参数...')
        return 0


def minus(*args):
    if len(args) > 1:
        m = 0
        for i in args:
            m -= i
        return m
    else:
        print('至少传入两个参数...')
        return 0


def mutiply(*args):
    pass


def divide(*args):
    pass


# 类
class Calculate:
    def __init__(self, num):
        self.num = num

    def test(self):
        print('正在使用Calculate进行计算...')

    @classmethod
    def test1(cls):
        print('——------>Calculate中的类方法')


def test():
    print('我是测试....')


# 在本模块执行时：__name__ -----> __main__
# 在被其他模块导入加载时：__name__ -----> 其他模块名
print('__name__', __name__)
if __name__ == '__main__':
    test()
