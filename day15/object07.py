# coding=utf-8
# @Time     :2020/4/26 0026 1:04
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :object07.py
# @Software :PyCharm

#  魔术方法
# __init__：初始化魔术方法
# 触发时间：初始化对象时触发（不是实例化触发，但是和实例化在一个操作中）

# __new__：实例化的魔术方法
# 触发时机：在实例化对象时触发

# __call__:对象调用方法
# 触发时机：将对象当成函数使用时候，会默认调用此函数内容

# __del__：delete的缩写  析构魔术方法

class Person:
    def __init__(self, name):
        print('------->init', self)  # <__main__.Person object at 0x0000021307D779B0>
        self.name = name

    def __new__(cls, *args, **kwargs):  # __new__向内存要空间 ---->地址
        print('————---->new')
        position = object.__new__(cls)
        print(position)  # <__main__.Person object at 0x0000021307D779B0>
        return position  # 地址

    def __call__(self, name):
        print('--------------->call')
        print('执行对象得到的参数是：', name)


p = Person('aa')

print(p)  # <__main__.Person object at 0x0000021307D779B0>

# 把对象当成函数来使用时，需要重写__call__，不当做函数时，不用写__call__
p('zhangwei')  # 执行对象得到的参数是： zhangwei
