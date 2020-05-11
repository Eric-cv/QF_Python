# coding=utf-8
# @Time     :2020/4/28 0028 0:28
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :object02.py
# @Software :PyCharm


class Student:
    # __age = 18 # 类属性

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__score = 50

    # 定义共有的set和get方法
    # set是为了赋值
    def setAge(self, age):
        if age > 0 and age < 120:
            self.__age = age
        else:
            print('年龄不在规定的范围内')

    # 修改名字的时候限制长度
    def setName(self, name):
        if len(name) == 6:
            self.__name = name
        else:
            print('名字不是6位')

    # get是为了取值
    def getAge(self):
        return self.__age

    def __str__(self):
        return '姓名:{},年龄{},考试分数{}'.format(self.__name, self.__age, self.__score)

    # attribute: getName setName __str __ __init__


s = Student('yupeng', 18)
print(s)
# dir是拿到attribute的列表
# ['_Student__age', '_Student__name', '_Student__score', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'getAge', 'setAge', 'setName']
print(dir(Student))
print(dir(s))
print(s._Student__age)  # 其实就是__age，只不过是系统自动改名字了
