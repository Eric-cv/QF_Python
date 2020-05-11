# coding=utf-8
# @Time     :2020/4/28 0028 1:00
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :object04.py
# @Software :PyCharm

# 继承：is a, has a
'''
公路(Road):
    属性：公路名称，公路长度

车(Car):
    属性：车名 时速
    方法：1.求车名在那条公路上以多少的时速行驶了多长时间
         get_time(self, road)

        2.初始化车属性信息__init__方法
        3.打印对象显示车的属性信息
'''

import random

# 定义Road类
class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


# 定义Car类
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


    def get_time(self, road): # road = r road与r是指向同一个地址空间的
        random_time = random.randint(1, 10)
        msg = '{}品牌的车在{}上以{}的速度行驶了{}小时'.format(self.brand, road.name, self.speed, random_time)
        print(msg)

    def __str__(self):
        return '{}品牌的，速度{}'.format(self.brand, self.speed)


# 创建实例对象
r = Road('京藏高速', 12000)
print(r.name)  # 京藏高速
r.name = '京哈高速'

audi = Car('奥迪', 120)
print(audi)  # 奥迪品牌的，速度120
audi.get_time(r)  # 对象















