# coding=utf-8
# @Time     :2020/4/30 0030 15:52
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :tst.py
# @Software :PyCharm

class Person:
    def __init__(self):
        self.__money = 200
        self.name = '匿名'

    def show1(self):
        print(self.name, self.__money)


class Student(Person):
    def __init__(self):
        # super().__init__()
        # super(Student, self).__init__()
        # Person().__init__(self)
        self.__money = 500

    def show(self):
        print('money', self.name)
        print('money', self.__money)


s = Student()
s.show()  # money 匿名  money 500
s.show1()  # money 200
