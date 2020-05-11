# coding=utf-8
# @time     :2020/4/30 0030 11:44
# @author   :eric
# @email    :zhangqi_@pku.edu.cn
# @file     :object08.py
# @software :pycharm

'''
编写一个简单的工资管理程序，系统可以管理以下四类人：工人(worker), 销售(salesman), 经理(manager), 销售经理(salemager)
所有的员工都具有员工号，姓名，工资等属性，有设置姓名，获取姓名，获取员工号，计算工资等方法，
1）工人：工人具有工作小时数和时薪的属性，工资计算方法为工作小时数*时薪
2）销售员：具有销售额和提成比例的属性，工资计算方法为销售额*提成比例
3）经理：具有固定月薪的属性，工资计算方法为固定月薪
4）销售经理：工资计算方法为销售额*提成比例：固定月薪
请根据以上要求设计合理的类，完成以下功能：
1）添加所有类型的人员
2）计算时薪
3）显示所有人工资情况
'''


class Person:
    def __init__(self, nu, name, salary):
        self.nu = nu
        self.name = name
        self.salary = salary

    def __str__(self):
        msg = '工号:{}, 姓名:{}, 本月工资:{}'.format(self.nu, self.name, self.salary)
        return msg

    def getsalary(self):
        return self.salary


class Worker(Person):
    def __init__(self, nu, name, salary, hours, per_hour_money):
        super().__init__(nu, name, salary)
        self.hours = hours
        self.per_hour_money = per_hour_money

    def getsalary(self):
        money = self.hours * self.per_hour_money
        self.salary += money
        return self.salary


class Salesman(Person):
    def __init__(self, nu, name, salary, salemoney, percent):
        super(Salesman, self).__init__(nu, name, salary)
        self.salemoney = salemoney
        self.percent = percent

    def getsalary(self):
        money = self.salemoney * self.percent
        self.salary += money
        return self.salary

# 创建子类对象
w = Worker('001', 'king', 2000, 100, 50)
s = w.getsalary()
print('月薪是：', s)
print(w)

saler = Salesman('002', 'lucy', 5000, 50000000, 0.003)
s = saler.getsalary()
print('月薪是', s)
print(saler)


