# coding=utf-8
# @Time     :2020/4/26 0026 21:40
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :object08.py
# @Software :PyCharm
import sys
'''
__del__:
1.对象赋值
    p = Person()
    p1=p
    p2=p
    说明：p和p1共同指向同一个地址
2.删除地址的引用
    del p1 删除对p1地址的引用
3.查看对地址的引用次数
    sys.getrefcount(p)
4.当一块空间没有任何引用(ref)，默认执行__del__
'''

class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('----------->del')


p = Person('jack')
p1 = p  # 与p是同一个地址
p2 = p  # 与p是同一个地址
print(p1.name)  # jack
print(p2.name)  # jack

p1.name = 'tom'
print(p.name)  # tom
print(p2.name)  #

del p2
print('删除p2后打印：', p.name)
print(sys.getrefcount(p))
del p1
print('删除p1后打印：', p.name)
print(sys.getrefcount(p))
# del p
# print('删除p后打印：', p.name)  # 报错  name 'p' is not defined
# print(sys.getrefcount(p))

# 对象赋值
n = 5
n1 = n
print(5)