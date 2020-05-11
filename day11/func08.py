# coding=utf-8
# @Time     :2020/4/13 0013 0:45
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :func08.py
# @Software :PyCharm

# 地址引用
a = 10  # 声明整型变量
b = a


def test_aa():  # 声明函数
    print('---------test----------')


# t = test
# print(t)

def func(f):
    print(f)
    f()
    print('------------------>func')


# 调用
func(test_aa)

'''
装饰器特点：
1.函数A是作为参数出现的，函数B就接收函数A作为参数
2.要有闭包的特点
'''


# 定义一个装饰器
def decorate(func):
    a = 100
    print('wrapper 外层打印测试')
    def wrapper():
        func()
        print('--------->刷漆')
        print('--------->铺地板', a)
        print('--------->装门')
    print('wrapper 加载完成')
    return wrapper


# 使用装饰器
@ decorate
def house():
    print('我是毛坯房.....')

'''
1.house被装饰函数（装饰器下的函数为被装饰函数）
2.将被装饰函数作为参数传给装饰器decorate
3.执行decorate函数代码
4.将装饰函数的返回值又赋值给house
'''
# 调用函数house
house()
