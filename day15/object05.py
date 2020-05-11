# coding=utf-8
# @Time     :2020/4/25 0025 23:49
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :object05.py
# @Software :PyCharm

# 类方法
'''
特点：
1.定义需要依赖装饰器 @classmethod
2.类方法中的参数不是一个对象，而是类
  print(cls)  # <class '__main__.Dog'>
3.类方法中只可以使用类属性（类方法是在对象还没有创建的时候就开始创建了，因此不能在方法中调用对象中的属性）
4.类方法中能不能调用普通方法？不能，因为普通方法需要调用self，而类方法中还没有创建self

类方法的作用：
因为只能访问类属性和类方法，所以可以在对象创建之前，如果需要完成一些动作(功能)
类方法不依赖对象，它是在对象创建之前创建，可以独立于对象做一些动作
'''

class Dog:
    def __init__(self, nickname):
        self.nickname = nickname

    def run(self):  # self 对象
        print('{}在院子里跑来跑去'.format(self.nickname))

    def eat(self):
        print('吃饭。。。。')
        self.run()  # 类中普通方法的互相调用，需要通过self.方法名()互相调用

    @classmethod  # 类方法，调用的时候传的是类，即Dog类的地址
    def test(cls):  # cls class
        print('----------')
        print(cls)  # <class '__main__.Dog'>
        # print(cls.nickname)  # AttributeError: type object 'Dog' has no attribute 'nickname'
        # print(self.nickname)  # 报错：类方法是在对象产生之前创建，因此无法得到self对象属性
        # self.run()  # 报错：类方法同样无法调用普通方法，因为self对象未创建


d = Dog('大黄')
d.run()  # 调用run
d.test()
