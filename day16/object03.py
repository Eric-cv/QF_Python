# coding=utf-8
# @Time     :2020/4/28 0028 0:37
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :object03.py
# @Software :PyCharm

# 在开发中看到一些私有化处理：装饰器

class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 先有getXXX
    @property
    def age(self):
        return self.__age

    # 再有setXXX，因为set依赖于get
    @age.setter
    def age(self, age):
        if age > 0 and age < 120:
            self.__age = age
        else:
            print('年龄不在规定的范围内')

    # def setAge(self, age):
    #     if age > 0 and age < 120:
    #         self.__age = age
    #     else:
    #         print('年龄不在规定的范围内')
    #
    # def setName(self, name):
    #     if len(name) == 6:
    #         self.__name = name
    #     else:
    #         print('名字不是6位')

    # # get是为了取值
    # def getAge(self):
    #     return self.__age

    def __str__(self):
        return '姓名:{},年龄{},考试分数{}'.format(self.__name, self.__age, self.__score)


s = Student('peng', 20)
s.name = 'xiaopeng'
print(s.name)  # xiaopeng

s.age = 130  # 使用装饰器进行私有化赋值，但是不满足判断条件
print(s.age)  # 20


