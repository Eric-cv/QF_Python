# coding=utf-8
# @Time     :2020/4/25 0025 22:18
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :object03.py
# @Software :PyCharm


class Person():
    # __init__中初始化对象的共同属性，在创建每个对象空间时，
    # 会在对象空间中自动定义这些属性，__init__也是函数，同样可以传参数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):  # 普通方法中也可以传参数
        print('{}，今年{}岁，正在跑步'.format(self.name, self.age))

    def run(self):
        print('{}，今年{}岁，正在跑步'.format(self.name, self.age))


p = Person('李四', 20)  # 实例初始化
p.name = 'lisi'  # 再次赋值更改初始化p空间中初始化的name的值
p.eat('红烧肉')
p.run()

p1 = Person('wangwu', 22)
p1.name = '王五'
p1.eat('狮子头')
p1.run()

p2 = Person('zhaoliu', 17)
p2.run()
