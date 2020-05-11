# coding=utf-8
# @Time     :2020/4/30 0030 10:31
# @Author   :Eric
# @Email    :zhangqi_@pku.edu.cn
# @File     :object07.py
# @Software :PyCharm
'''
继承：
 Student, Employee, Doctor ----> 都属于人类
 相同的代码 ----> 代码冗余，可读性不高
 将相同的代码提取 ----> Person类
 Student, Employee, Doctor ---->继承Person
 class Student(Person):
    pass
特点：
    1.如果类中不定义__init__，调用父类super class的__init__
    2.如果类继承了父类也需要定义自己的__init__，就需要在子类的__init__中调用一下父类的__init__
    3.如何调用父类的__init__:
        super().__init__(参数)
        super(类名, 对象).__init__(参数)
    4.如果父类有eat()，子类也定义一个eat方法，默认搜索的原则:先找当前类，再去找父类
    s.eat()
    overrider  重写(覆盖)
    父类提供的方法不能满足子类的需求，就需要在子类中定义一个同名的方法，这种行为：重写
    5.子类的方法中也可以调用父类方法(与init方法中继承父类的魔术方法init一样，普通方法也可以继承父类的普通方法)：
    super().方法名(参数)
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭...')

    def run(self):
        print(self.name + '正在跑步')


class Student(Person):
    def __init__(self, name, age, classnumber):
        super().__init__(name, age)
        self.classnumber = classnumber

    def study(self, course):
        print('{}正在学习{}课程'.format(self.name, course))

    def eat(self, food):  # 子类中有和父类同名的方法，优先调用子类方法，搜索原则：类本身-->父类
        super().eat()  # 重写的时候如果有需要，也可以把父类的代码调过来
        print(self.name + '正在吃饭...喜欢吃：' + food)


class Employee(Person):
    def __init__(self, name, age, salary, manager):
        super().__init__(name, age)
        self.salary = salary
        self.manager = manager


class Doctor(Person):
    def __init__(self, name, age, patients):
        super(Doctor, self).__init__(name, age)
        self.patients = patients


s = Student('阿文', 18, 'python1905')
s.run()  # 阿文正在跑步
s.study('python基础')  # 阿文正在学习python基础课程
s.eat('满汉全席')  # 阿文正在吃饭...喜欢吃：满汉全席
e = Employee('tom', 23, 10000, 'king')
e.run()  # tom正在跑步

lists = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
d = Doctor('lucy', 30, lists)
d.run()  # lucy正在跑步
