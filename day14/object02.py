# coding=utf-8
# @time     :2020/4/25 0025 16:09
# @author   :eric
# @email    :zhangqi_@pku.edu.cn
# @file     :object02.py
# @software :pycharm

# 定义类和属性
class Student:
    # 类属性
    name = 'xiaowei'
    age = 2


# 使用类，创建对象  对象 = 类名()
xiaowei = Student()
# 搜索原则：
# 1)先找自己空间的，再去模型空间中找，
# 2)如果自己的空间中存在属性，则不会去模型中查找
print(xiaowei.name)  # xiaowei 模型空间
print(xiaowei.age)  # 2 模型空间
# print(xiaowei.gender)  # attributeerror: 'student' object has no attribute 'gender'
xiaowei.age = 18  # 在自己空间创建属性，与类属性不同，为对象属性
print(xiaowei.age)  # 18 自己空间


yupeng = Student()
print(yupeng.name)
yupeng.name = 'xiaopengpeng'
print(yupeng.name)
print(yupeng.age)
yupeng.age = 1
print(yupeng.age)

Student.name = 'feifei'
ruirui = Student()
print(ruirui.name)