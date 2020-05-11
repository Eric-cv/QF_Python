# coding=utf-8
# @Time     :2020/4/27 0027 23:38
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :object01.py
# @Software :PyCharm

# 私有化
# 封装：1.私有化属性 2.定义共有的set和get方法
# __属性: 就是将属性私有化，访问范围仅仅限于类中
'''
好处：
1.隐藏属性不被外界随意修改
2.也可以修改：通过函数
    def setXXX(self, xxx):
        3.筛选赋值的内容
          if xxx是否符合条件
                赋值
          else:
               不赋值
3.如果想获取具体的某一个属性
    使用get函数
    def getXXX(self):
        return self.XXX

'''

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


yupeng = Student('yupeng', 18)
print(yupeng)  # 姓名:yupeng,年龄18,考试分数50
yupeng.setAge(120)  # 年龄不在规定的范围内
print(yupeng)  # 姓名:yupeng,年龄18,考试分数50
yupeng.setName('xiaopeng')  # 名字不是6位
print(yupeng)  # 姓名:yupeng,年龄18,考试分数50

# 就想拿到于鹏的年龄
print(yupeng.getAge())  # 18
print(yupeng.__score)  # AttributeError: 'Student' object has no attribute '__score'

